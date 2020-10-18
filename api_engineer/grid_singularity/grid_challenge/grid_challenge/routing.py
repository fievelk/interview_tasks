"""Django channels routing."""

# from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import grid_api.routing


application = ProtocolTypeRouter({
    'websocket': URLRouter(grid_api.routing.websocket_urlpatterns)})
