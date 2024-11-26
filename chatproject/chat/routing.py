from django.urls import path
from . import consumers

ASGI_urlpatterns = [
    path("websocket/<str:name>", consumers.ChatConsumer.as_asgi() ),

]