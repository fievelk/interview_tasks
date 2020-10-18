from django.db import models

from grid_api.simulations import test_sim


class Simulation(models.Model):
    """Model representing a simulation."""

    active_power = models.FloatField()
    reactive_power = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def run(self):
        """Run the simulation and store its results as instance variables.

        NOTE: this will not automatically persist the results.

        """
        self.active_power, self.reactive_power = test_sim.run_simulation()
