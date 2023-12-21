from django.urls import path
from . import views
from django.shortcuts import render

def popup(request):
    return render(request, './account/popup.html')

urlpatterns = [
    path('', views.index, name='home'),
    path('popup/', popup, name='popup'),
]