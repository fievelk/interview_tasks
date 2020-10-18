"""Exceptions module"""


from rest_framework import status
from rest_framework.exceptions import APIException

from grid_api import messages


class SimulationNotFoundException(APIException):
    """Json exception for not-found Simulation objects"""

    status_code = status.HTTP_404_NOT_FOUND
    default_detail = messages.RESOURCE_NOT_FOUND
    default_code = 'resource_unavailable'
