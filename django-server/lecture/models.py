from django.db import models
from config import asset_storage

s3_storage = asset_storage.MediaStorage()


# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/', null=True,
                            verbose_name="", storage=s3_storage)

    def __str__(self):
        return self.name
