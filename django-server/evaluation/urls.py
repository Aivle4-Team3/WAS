from django.urls import path
from . import views


urlpatterns = [
    path('<str:lecture_name>/<str:video_name>', views.evaluation, name='evaluation'),
]
