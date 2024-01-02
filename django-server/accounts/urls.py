from django.urls import path, include
from . import views

from allauth.socialaccount import views as socialaccount_views
from allauth.account.views import LoginView, LogoutView, PasswordResetView

# Create your views here.


urlpatterns = [
    path('login/', LoginView.as_view(), name='account_login'),
    path('login_success/', views.login_success, name='login_success'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('password/reset/', PasswordResetView.as_view(),
         name='account_reset_password'),
    path('', include('allauth.urls')),
    path('signup/', socialaccount_views.SignupView.as_view(),
         name='account_signup'),
    path('consent/', views.consent, name='consent' ),
]
