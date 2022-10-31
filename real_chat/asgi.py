"""
ASGI config for real_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import room.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_chat.settings')
django.setup()
application = ProtocolTypeRouter(
    {
        "http":get_asgi_application(),
        "websocket":AuthMiddlewareStack(
            URLRouter(
                room.routing.websocket_urlpatterns))
    }
)
