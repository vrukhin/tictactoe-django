from django.shortcuts import redirect, render, get_object_or_404

from .models import Room
from .forms import RoomForm


def index(request):
    return render(request, 'tictac/index.html')


def rooms_list(request):
    rooms = Room.objects.all()
    return render(
        request,
        'tictac/rooms.html',
        {'rooms':rooms},
        )


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(
        request,
        'tictac/room_detail.html',
        {'room':room},
        )


def room_create(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    else:
        form = RoomForm()
    return render(request, 'tictac/create.html', {'form': form})
