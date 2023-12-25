from django.db import models
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
permission = GoogleDriveFilePermission(
    GoogleDrivePermissionRole.READER,
    GoogleDrivePermissionType.ANYONE
)

gd_storage = GoogleDriveStorage(permissions=(permission, ))


# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=100, null=True)
    file = models.FileField(upload_to='videos/', null=True,
                            verbose_name="", storage=gd_storage)

    def __str__(self):
        return self.name
