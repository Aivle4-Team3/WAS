from django.urls import path, include
from allauth.account.views import LoginView, LogoutView, PasswordResetView
from .views import login_success, CustomSignupView

# Create your views here.


urlpatterns = [
    path('login/', LoginView.as_view(), name='account_login'),
    path('login_success/', login_success, name='login_success'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('password/reset/', PasswordResetView.as_view(),
         name='account_reset_password'),
    path('signup/', CustomSignupView.as_view(),
         name='account_signup'),
    path('', include('allauth.urls')),  # 오버라이딩할 때 순서 잘 생각하자...
]
