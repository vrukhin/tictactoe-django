from .models import Room
from django.forms import ModelForm


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'room_description']
        labels = {
            'room_name': 'Название комнаты',
            'room_description': 'Описание',
        }

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'text-field'
