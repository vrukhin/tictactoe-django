from django.shortcuts import render, get_object_or_404

from .models import Room


def index(request):
    return render(request, 'tictac/index.html')


def rooms_list(request):
    rooms = Room.objects.all()
    return render(
        request,
        'tictac/rooms.html',
        {'rooms':rooms},
        )


def room_detail(request, id):
    room = get_object_or_404(Room, id=id)
    return render(
        request,
        'tictac/room_detail.html',
        {'room':room},
        )


def create(request):
    return render(request, 'tictac/create.html')
