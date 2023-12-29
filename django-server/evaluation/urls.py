from django.urls import path
from . import views


urlpatterns = [
    path('', views.evaluation, name='evaluation'),
    path('<int:video1>/', views.evaluation1, name='evaluation1'),
]
