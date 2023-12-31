from django.db import models
from lecture.models import Lecture

# Create your models here.

class Message(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.DO_NOTHING)
    user_message = models.TextField()
    bot_message = models.TextField()