from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms', views.rooms_list, name='rooms'),
    path('rooms/<int:room_id>', views.room_detail, name='room_detail'),
    path('rooms/create', views.room_create, name='room_create'),
]
