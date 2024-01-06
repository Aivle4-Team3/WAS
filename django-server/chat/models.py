from django.db import models
from pgvector.django import VectorField
from lecture.models import Enrollment

# Create your models here.


class Message(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, null=False, related_name='messages')

    user_time = models.DateTimeField(null=True)
    bot_time = models.DateTimeField(null=True)

    user_message = models.TextField()
    bot_message = models.TextField()
    user_message_embedded = VectorField(dimensions=1536)
    bot_message_embedded = VectorField(dimensions=1536)
