from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    country = models.CharField(max_length=15, null=True)
    phone_number = PhoneNumberField(null=True, region='KR')
    avatar = models.ImageField(upload_to="avatar/", default="default_avatar.jpg")
