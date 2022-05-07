from .models import Room
from django.forms import ModelForm


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'room_description']
