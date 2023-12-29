from django.urls import path
from . import views


urlpatterns = [
    path('<str:lecture_name>', views.chatpage, name='chat'),

]
