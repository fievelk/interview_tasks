from django.urls import re_path

from grid_api import consumers

websocket_urlpatterns = [
    re_path(r'ws/simulations/$', consumers.SimulationConsumer),
]
