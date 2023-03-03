from django.shortcuts import render, redirect
import uuid
import boto3
from django.views.generic.edit import CreateView
from .models import Board, Photo

S3_BASE_URL = 'https://s3.amazonaws.com/'
BUCKET = 'inspoboarddjangoapp'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def boards_index(request):
    boards = Board.objects.all()
    return render(request, 'boards/index.html', {'boards': boards})

def boards_details(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, 'boards/details.html', {'board': board})

class BoardCreate(CreateView):
    model = Board
    fields = '__all__'


def add_photo(request, board_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to board_id or board (if you have a board object)
            photo = Photo(url=url, board_id=board_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('details', board_id=board_id)
