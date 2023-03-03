from django.shortcuts import render, redirect
import uuid
import boto3
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Board, Tag, Photo

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

    tags = Tag.objects.all()
    tags_board_doesnt_have = tags.exclude(id__in = board.tags.all().values_list('id'))

    return render(request, 'boards/details.html', {'board': board, 'tags': tags_board_doesnt_have})

def assoc_tag(request, board_id, tag_id):
  Board.objects.get(id=board_id).tags.add(tag_id)
  return redirect('details', board_id=board_id)

def unassoc_tag(request, board_id, tag_id):
  Board.objects.get(id=board_id).tags.remove(tag_id)
  return redirect('details', board_id=board_id)

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

class BoardCreate(CreateView):
    model = Board
    fields = ['name', 'description']

class BoardUpdate(UpdateView):
    model = Board
    fields = ['name', 'description']
    
class BoardDelete(DeleteView):
    model = Board
    success_url = '/boards/'

class TagList(ListView):
    model = Tag
    template_name = 'tag_pages/index.html'

    def get_all(self):
      return Tag.objects.all()

class TagDetail(DetailView):
  model = Tag
  template_name = 'tag_pages/details.html'

class TagCreate(CreateView):
  model = Tag
  fields = '__all__'

class TagUpdate(UpdateView):
    model = Tag
    fields = '__all__'

class TagDelete(DeleteView):
    model = Tag
    success_url = '/tags/'