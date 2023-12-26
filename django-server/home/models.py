from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta
from config import asset_storage
from storages.backends.s3boto3 import S3Boto3Storage

s3_storage = asset_storage.MediaStorage()


# Create your models here.

class Lecture(models.Model):
    thumbnail = models.ImageField(
        upload_to="images/", default="default_thumbnail.jpg", storage=s3_storage)
    chapter = models.CharField(max_length=10, default="")
    grade = models.SmallIntegerField(validators=[MinValueValidator(0),
                                                 MaxValueValidator(5)], default=5)
    visited = models.IntegerField(default=0)
    title = models.CharField(max_length=100, default="")
    summary = models.TextField(default="")
    reamin_time = models.DurationField(default=timedelta)

    def __str__(self):
        return self.title
