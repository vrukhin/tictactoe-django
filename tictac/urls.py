from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms', views.rooms, name='rooms'),
    path('rooms/create', views.create, name='create'),
]
