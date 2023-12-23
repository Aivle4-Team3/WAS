from django.urls import path
from . import views
from accounts import views as accounts_view


urlpatterns = [
    path('', views.index, name='home'),
    path('mypage', accounts_view.mypage, name='mypage'),
]
