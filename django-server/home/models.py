from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta
from config import asset_storage
from storages.backends.s3boto3 import S3Boto3Storage

s3_storage = asset_storage.MediaStorage()


# Create your models here.

class Lecture(models.Model):
    title = models.CharField(max_length=100, default="")
    subject = models.CharField(max_length=10, default="")
    teacher = models.CharField(max_length=10, default="")
    thumbnail = models.ImageField(upload_to="images/", default="default_thumbnail.jpg", storage=s3_storage)
    summary = models.TextField(default="")
    student_count = models.IntegerField(default=0)
    rating = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=5)
    remain_time = models.DurationField(default=timedelta)

    def __str__(self):
        return self.title
