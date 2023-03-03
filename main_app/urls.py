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
]