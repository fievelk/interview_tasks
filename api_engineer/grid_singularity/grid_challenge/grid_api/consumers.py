import json
from channels.generic.websocket import WebsocketConsumer
from django.conf import settings

from grid_api.serializers import SimulationSerializer
from grid_api.models import Simulation

from grid_api import messages

from asgiref.sync import async_to_sync


class SimulationConsumer(WebsocketConsumer):
    def connect(self):
        """
        Join the main websocket group, accept the connection and return the
        latest Simulation.

        """
        async_to_sync(self.channel_layer.group_add)(
            settings.DEFAULT_WS_GROUP,
            self.channel_name)

        self.accept()
        self.send_latest_simulation()

    def disconnect(self, close_code):
        """Leave the websocket group."""

        async_to_sync(self.channel_layer.group_discard)(
            settings.DEFAULT_WS_GROUP,
            self.channel_name)

    def send_latest_simulation(self, event=None):
        """Send the latest simulation to the websocket group."""

        try:
            simulation = Simulation.objects.latest('pk')
        except Simulation.DoesNotExist:
            return self.send(text_data=json.dumps(
                {'message': messages.RESOURCE_NOT_FOUND}))

        serializer = SimulationSerializer(simulation)
        self.send(text_data=json.dumps(serializer.data))
