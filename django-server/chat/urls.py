from django.urls import path
from . import views


urlpatterns = [
    path('', views.chatpage, name='chat'),
    
    path('chatservice', views.chatservice),
    path("<str:room_name>/", views.room, name="room"),
]