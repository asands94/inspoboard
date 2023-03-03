from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('boards/', views.boards_index, name='index'),
  path('boards/<int:board_id>/', views.boards_details, name ='details'),
  path('boards/create/', views.BoardCreate.as_view(), name='board_create'),
  path('boards/<int:pk>/update/', views.BoardUpdate.as_view(), name='board_update'),
  path('boards/<int:pk>/delete/', views.BoardDelete.as_view(), name='board_delete'),
  path('boards/<int:board_id>/add_photo/', views.add_photo, name='add_photo'),
  path('boards/<int:board_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
  path('boards/<int:board_id>/assoc_tag/<int:tag_id>/remove/', views.unassoc_tag, name='unassoc_tag'),
  path('tags/', views.TagList.as_view(), name='tags_index'),
  path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags_details'),
  path('tags/create/', views.TagCreate.as_view(), name='tags_create'),
  path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tags_update'),
  path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tags_delete'),
]