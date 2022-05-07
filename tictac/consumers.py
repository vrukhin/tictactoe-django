import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from tictac.models import Room


class RoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_id = 'tictac_%s' % self.room_id

        await self.channel_layer.group_add(
            self.room_group_id,
            self.channel_name,
        )

        await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_id,
            self.channel_name,
        )


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        player = text_data_json['player']
        cell = text_data_json['cell']

        await self.make_move(cell, player)

        await self.channel_layer.group_send(
            self.room_group_id,
            {
                'type': 'room_message',
                'player': player,
                'cell': cell,
            }
        )


    async def room_message(self, event):
        player = event['player']
        cell = event['cell']
        await self.send(text_data=json.dumps({
            'player': player,
            'cell': cell,
        }))

    
    @database_sync_to_async
    def make_move(self, cell, player):
        id = int(cell.split('-')[1])
        r = Room.objects.get(pk=self.room_id)
        room_state = r.room_state
        room_state_new = room_state[:id] + player + room_state[id+1:]
        r.room_state = room_state_new
        r.save()
