from django.db import models

# Create your models here.

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField()
    thumbnail = models.ImageField(upload_to="uploads/", default="default_thumbnail.jpg")