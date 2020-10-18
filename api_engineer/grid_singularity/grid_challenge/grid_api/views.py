from django.http import JsonResponse

from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from grid_api.exceptions import SimulationNotFoundException
from grid_api.models import Simulation
from grid_api.serializers import SimulationSerializer


@api_view(['POST'])
def launch_simulation(request):
    # Create a simulation object (not persisted)
    simulation = Simulation()
    simulation.run()
    simulation.save()

    serializer = SimulationSerializer(simulation)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def simulation_detail(request, pk):
    """Retrieve a Simulation object."""

    try:
        simulation = Simulation.objects.get(pk=pk)
    except Simulation.DoesNotExist:
        raise SimulationNotFoundException()

    if request.method == 'GET':
        serializer = SimulationSerializer(simulation)
        return JsonResponse(serializer.data)


@api_view(['GET'])
def get_last(request):
    """Retrieve the last Simulation object."""

    serializer = SimulationSerializer(_fetch_last_simulation())

    return JsonResponse(serializer.data)


@api_view(['GET'])
def get_last_active_power(request):
    """
    GET request that reads the active power of the previously executed
    simulation.

    """
    return Response(_fetch_last_simulation().active_power)


@api_view(['GET'])
def get_last_reactive_power(request):
    """
    GET request that reads the reactive power of the previously executed
    simulation.

    """
    return Response(_fetch_last_simulation().reactive_power)


def _fetch_last_simulation():
    try:
        return Simulation.objects.latest('pk')
    except Simulation.DoesNotExist:
        raise SimulationNotFoundException()
