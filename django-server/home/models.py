from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import timedelta

# Create your models here.

from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage

permission = GoogleDriveFilePermission(
    GoogleDrivePermissionRole.READER,
    GoogleDrivePermissionType.ANYONE
)

gd_storage = GoogleDriveStorage(permissions=(permission, ))


class Lecture(models.Model):
    thumbnail = models.ImageField(
        upload_to="images/", default="default_thumbnail.jpg", storage=gd_storage)
    chapter = models.CharField(max_length=10, default="")
    grade = models.SmallIntegerField(validators=[MinValueValidator(0),
                                                 MaxValueValidator(5)], default=5)
    visited = models.IntegerField(default=0)
    title = models.CharField(max_length=100, default="")
    summary = models.TextField(default="")
    reamin_time = models.DurationField(default=timedelta)
