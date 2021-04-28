from django.urls import re_path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer),
]

# chat/routing.py
#from django.conf.urls import url

#from . import consumers

#websocket_urlpatterns = [
   # url('ws/chat/<str:room_name>/$', consumers.ChatConsumer),
#]