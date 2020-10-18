from django.apps import AppConfig


class GridApiConfig(AppConfig):
    name = 'grid_api'

    def ready(self):
        """Import the signals module (e.g. to dispatch post_save signals)."""

        import grid_api.signals
