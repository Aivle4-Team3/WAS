from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta
from config import asset_storage
from accounts.models import User

s3_storage = asset_storage.MediaStorage()


# Create your models here.

class Lecture(models.Model):    
    title = models.CharField(max_length=100, default="")
    title_info = models.CharField(max_length=1000, default="")
    subject = models.CharField(max_length=10, default="")
    teacher = models.ForeignKey(User, limit_choices_to={"groups__name": "선생"}, on_delete=models.DO_NOTHING, null=True, blank=True)
    thumbnail = models.ImageField(upload_to="images/", default="default_thumbnail.jpg", storage=s3_storage)
    summary = models.TextField(default="")
    student_count = models.IntegerField(default=0)
    rating = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=5)
    remain_time = models.DurationField(default=timedelta)

    def __str__(self):
        return self.title

class Video(models.Model):
    lecture = models.ForeignKey(Lecture, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/', null=True,
                            verbose_name="", storage=s3_storage)
    video_duration = models.DurationField(default=timedelta)

    def __str__(self):
        return self.name