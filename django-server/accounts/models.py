from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    country = models.CharField(max_length=15, null=True)
    phone_number = PhoneNumberField(null=True, region='KR')
    avatar = models.ImageField(upload_to="avatar/", default="default_avatar.jpg")


# 유저별 알림 메시지
class UserMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
