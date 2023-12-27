from django.urls import path
from . import views


urlpatterns = [
    path('', views.board, name='board'),
    path('<int:no>/', views.detail, name='detail'),
    path('test1/', views.test1), # views.py에 정의함, 함수 or 클래스
    path('test2/<int:no>/', views.test2), # int로 바꾸고 싶으면 int:no
    path('profile/', views.profile),
    path('tag/<id>/', views.tag_list),
    path('test3/', views.test3),
    path('new/', views.post_create, name='create'),
    path('update/<id>/', views.post_update, name='update'),
    path('delete/<id>/', views.post_delete, name='delete'),
]
