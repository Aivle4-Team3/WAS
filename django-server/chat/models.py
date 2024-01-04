from django.db import models
from lecture.models import Video
from accounts.models import User
from pgvector.django import VectorField

# Create your models here.


class Message(models.Model):
    # user-video : message 다대다 관계 필드
    user_and_video = models.ManyToManyField(
        'UserAndVideoRelation', related_name='messages')

    user_time = models.DateTimeField(null=True)
    bot_time = models.DateTimeField(null=True)

    user_message = models.TextField()
    bot_message = models.TextField()
    user_message_embedded = VectorField(dimensions=1536)
    bot_message_embedded = VectorField(dimensions=1536)


class UserAndVideoRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
