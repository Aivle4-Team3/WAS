from django.urls import path
from . import views
from .models import QnA
from .forms import QnAModelForm


app_name = 'qna'
view = views.Which(QnA, QnAModelForm, app_name)


urlpatterns = [
    path('', view.board, name='qna'),
    path('<int:no>/', view.detail, name='detail'),

    path('new/', view.post_create, name='create'),
    path('update/<id>/', view.post_update, name='update'),
    path('delete/<id>/', view.post_delete, name='delete'),
    path('<int:id>/create/comment/', view.create_comment, name="create_comment"),
    path('<int:id>/delete/comment/<int:comment_id>/',
         view.delete_comment, name="delete_comment"),
]
