from django.urls import path, include
from allauth.account.views import LoginView, LogoutView, PasswordResetView
from .views import CustomSignupView, mypage, faq

# Create your views here.


urlpatterns = [
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('signup/', CustomSignupView.as_view(), name='account_signup'),
    path('password/reset/', PasswordResetView.as_view(), name='account_reset_password'),
    path('mypage', mypage, name='mypage'),
    path('faq', faq, name='faq'),
    path('', include('allauth.urls')),  # 오버라이딩할 때 순서 잘 생각하자...
]
