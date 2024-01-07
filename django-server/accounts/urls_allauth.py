from django.urls import path, include
from allauth.account.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('', include('allauth.urls')),
]
