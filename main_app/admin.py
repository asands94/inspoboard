from django.contrib import admin
from .models import Board, Tag, Photo

# Register your models here.
admin.site.register(Board)
admin.site.register(Tag)
admin.site.register(Photo)