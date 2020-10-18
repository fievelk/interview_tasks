import json

from asgiref.sync import sync_to_async

from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings

from grid_api import messages
from grid_api.serializers import SimulationSerializer
from grid_api.models import Simulation


class SimulationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Join the main websocket group, accept the connection and return the
        latest Simulation.

        """
        await self.channel_layer.group_add(
            settings.DEFAULT_WS_GROUP,
            self.channel_name)

        await self.accept()
        await self.send_latest_simulation()

    async def disconnect(self, close_code):
        """Leave the websocket group."""

        await self.channel_layer.group_discard(
            settings.DEFAULT_WS_GROUP,
            self.channel_name)

    @staticmethod
    def get_latest_simulation():
        return sync_to_async(Simulation.objects.latest, thread_sensitive=True)('pk')

    async def send_latest_simulation(self, event=None):
        """Send the latest simulation to the websocket group."""

        try:
            simulation = await self.get_latest_simulation()
        except Simulation.DoesNotExist:
            await self.send(text_data=json.dumps(
                {'message': messages.RESOURCE_NOT_FOUND}))

        serializer = SimulationSerializer(simulation)
        await self.send(text_data=json.dumps(serializer.data))
