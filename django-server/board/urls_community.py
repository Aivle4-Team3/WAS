from django.urls import path
from . import views
from .models import Community
from .forms import CommunityModelForm


app_name = 'community'
view = views.Which(Community, CommunityModelForm, app_name)


urlpatterns = [
    path('', view.board, name='community'),
    path('<int:no>/', view.detail, name='detail'),

    path('new/', view.post_create, name='create'),
    path('update/<id>/', view.post_update, name='update'),
    path('delete/<id>/', view.post_delete, name='delete'),
    path('<int:id>/create/comment/', view.create_comment, name="create_comment"),
    path('<int:id>/delete/comment/<int:comment_id>/',
         view.delete_comment, name="delete_comment"),
]
