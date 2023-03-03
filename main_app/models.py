from django.db import models
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tags_details', kwargs={'pk': self.id})

class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('details', kwargs={'board_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for board_id: {self.board_id} @{self.url}"
