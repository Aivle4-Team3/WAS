from django.urls import path
from . import views


urlpatterns = [
    path('', views.showcase, name='lecture'),
    path('saveplayback/', views.save_playback, name='saveplayback'),
    path('<str:lecture_name>/', views.room, name='room'),
]
