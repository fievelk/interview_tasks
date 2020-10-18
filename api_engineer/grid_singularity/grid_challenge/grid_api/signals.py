from asgiref.sync import async_to_sync

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

import channels.layers

from grid_api.models import Simulation


@receiver(post_save, sender=Simulation)
def send_websocket_message(sender, **kwargs):
    """Send a websocket message everytime a Simulation instance is saved."""

    # Retrieve the channels layer (where the websocket will output its message)
    channel_layer = channels.layers.get_channel_layer()

    # Send a message to the entire websocket group
    async_to_sync(channel_layer.group_send)(
        settings.DEFAULT_WS_GROUP, {'type': 'send_latest_simulation'})
