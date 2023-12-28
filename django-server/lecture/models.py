from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta
from config import asset_storage

s3_storage = asset_storage.MediaStorage()


# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/', null=True,
                            verbose_name="", storage=s3_storage)

    def __str__(self):
        return self.name

class Lecture(models.Model):    
    title = models.CharField(max_length=100, default="")
    subject = models.CharField(max_length=10, default="")
    teacher = models.CharField(max_length=10, default="")
    thumbnail = models.ImageField(upload_to="images/", default="default_thumbnail.jpg", storage=s3_storage)
    summary = models.TextField(default="")
    student_count = models.IntegerField(default=0)
    rating = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=5)
    remain_time = models.DurationField(default=timedelta)
    
    video = models.ForeignKey(Video, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
