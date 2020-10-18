from django.urls import path
from grid_api import views

app_name = 'api'

urlpatterns = [
    path('simulations/', views.launch_simulation),
    path('simulations/last', views.get_last),
    path('simulations/last_active_power', views.get_last_active_power),  # TODO: use ?field=active_power
    path('simulations/last_reactive_power', views.get_last_reactive_power),
    path('simulations/<int:pk>', views.simulation_detail),
]
