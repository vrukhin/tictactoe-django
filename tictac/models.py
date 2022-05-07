from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=16)
    room_description = models.CharField(max_length=200)
    room_state = models.CharField(max_length=9, default='---------')
