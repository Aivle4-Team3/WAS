from django.db import models
from lecture.models import Video
from accounts.models import User

# Create your models here.


class TestPaper(models.Model):
    video = models.ForeignKey(Video, null=False, on_delete=models.CASCADE, related_name='testpapers')
    question = models.TextField(default="")
    answer = models.TextField(default="")
    
class TestResult(models.Model):
    testpaper = models.ForeignKey(TestPaper, null=False, on_delete=models.CASCADE)
    evaluation_date = models.DateField(auto_now_add=True)
    scrore = models.IntegerField(default=0)