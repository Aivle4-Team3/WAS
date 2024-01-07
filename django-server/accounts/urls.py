from django.urls import path, include
from allauth.account.views import PasswordResetView
from . import views

app_name = "accounts"
# Create your views here.
urlpatterns = [
    path('password/reset/', PasswordResetView.as_view(), name='reset_password'),
    path('mypage/', views.mypage, name='mypage'),
    path('consent/', views.consent, name='consent'),
    path('delete/', views.delete, name='delete'),
    path('readmessage/', views.read_message, name='readmessage'),
    path('', include('allauth.urls')),  # 오버라이딩할 때 순서 잘 생각하자...
]
