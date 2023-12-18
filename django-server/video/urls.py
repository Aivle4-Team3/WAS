from django.urls import path
from . import views


urlpatterns = [
    path('<str:video_name>/', views.video, name='video'),
]