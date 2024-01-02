from django.urls import path
from . import views


app_name = 'board'

urlpatterns = [
    path('', views.board, name='board'),
    path('<int:no>/', views.detail, name='detail'),
    
    path('new/', views.post_create, name='create'),
    path('update/<id>/', views.post_update, name='update'),
    path('delete/<id>/', views.post_delete, name='delete'),
    path('<int:id>/create/comment/', views.create_comment, name="create_comment"),
    path('<int:post_id>/delete/comment/<int:comment_id>/', views.delete_comment, name="delete_comment"),
]
