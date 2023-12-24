from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta

# Create your models here.


class Lecture(models.Model):
    thumbnail = models.ImageField(
        upload_to="images/", default="default_thumbnail.jpg")
    chapter = models.CharField(max_length=10, default="")
    grade = models.SmallIntegerField(validators=[MinValueValidator(0),
                                                 MaxValueValidator(5)], default=5)
    visited = models.IntegerField(default=0)
    title = models.CharField(max_length=100, default="")
    summary = models.TextField(default="")
    reamin_time = models.DurationField(default=timedelta)
