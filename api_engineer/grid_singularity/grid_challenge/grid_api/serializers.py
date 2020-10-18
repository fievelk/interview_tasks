# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from grid_api.models import Simulation


class SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulation
        fields = ['id', 'active_power', 'reactive_power']
