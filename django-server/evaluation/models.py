from django.db import models
from lecture.models import Video

# Create your models here.


class TestPaper(models.Model):
    video = models.ForeignKey(Video, null=False, on_delete=models.CASCADE, related_name='testpapers')
    question = models.TextField(default="")
    answer = models.TextField(default="")
