from django.db import models

# Create your models here.


class Video(models.Model):
    name = models.CharField(max_length=100, null=True)
    file = models.FileField(upload_to='videos/', null=True, verbose_name="")
