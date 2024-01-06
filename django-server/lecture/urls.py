from django.urls import path
from .views import lecture, save_playback


urlpatterns = [
    path('saveplayback/', save_playback, name='saveplayback'),
    path('<str:lecture_name>/', lecture, name='lecture'),
]
