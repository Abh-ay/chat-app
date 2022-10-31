from django.urls import path
from room.consumers import ChatConsumer

websocket_urlpatterns=[
    path('ws/<str:room_name>/',ChatConsumer.as_asgi())
    # re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
]