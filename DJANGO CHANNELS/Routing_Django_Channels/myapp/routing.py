from django.urls import path
from . import consumers

websocket_urlspatterns = [
    path('ws/sc/', consumers.SyncConsumer.as_asgi()),
    path('ws/ac/', consumers.AsyncConsumer.as_asgi()),
]
