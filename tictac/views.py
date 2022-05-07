from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'tictac/index.html')

def rooms(request):
    return render(request, 'tictac/rooms.html')
