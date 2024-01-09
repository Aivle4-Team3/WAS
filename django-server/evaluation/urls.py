from django.urls import path
from . import views


urlpatterns = [
    path('', views.my_evaluation, name='my_evaluation'),
    path('<str:lecture_name>/<str:video_name>', views.evaluation, name='evaluation'),
]
