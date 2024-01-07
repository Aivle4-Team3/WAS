from django.urls import path
from . import views


app_name = 'chat'

urlpatterns = [
    path('<str:lecture_name>/<str:video_name>', views.chat, name='page'),

]
