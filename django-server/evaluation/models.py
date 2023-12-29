from django.db import models
from lecture.models import Video

# Create your models here.
class Test(models.Model):
    video = models.ForeignKey(Video, null=True, on_delete=models.CASCADE)
    question = models.TextField(default="")
    answer = models.TextField(default="")
    