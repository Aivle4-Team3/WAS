from django.db import models
from lecture.models import Video
from pgvector.django import VectorField

# Create your models here.

class Message(models.Model):
    video = models.ForeignKey(Video, on_delete=models.DO_NOTHING, null=True)
    user_message = models.TextField()
    bot_message = models.TextField()
    user_message_embedded = VectorField(dimensions=1536)
    bot_message_embedded = VectorField(dimensions=1536)