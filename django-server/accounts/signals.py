from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.core.files.base import ContentFile
import requests


# 소셜 계정으로 가입 시 시그널
@receiver(user_signed_up)
def populate_profile(request, sociallogin=None, **kwargs):
    if sociallogin:
        # user 모델에 소셜 계정 데이터 추가
        user = sociallogin.account.user

        # 구글 프로필 이미지
        url = (sociallogin.account.extra_data.get('picture')
               # 네이버 프로필 이미지
               or sociallogin.account.extra_data.get('profile_image'))
        response = requests.get(url)

        if response.status_code == 200:
            user.avatar.save(user.username+'.jpg',
                             # ContentFile을 사용하여 이미지 저장
                             ContentFile(response.content), save=True)

        user.save()


# 가입 후 저장 시그널
@receiver(post_save, sender=get_user_model())
def set_default_group(sender, instance, created, **kwargs):
    if created:
        default_group, _ = Group.objects.get_or_create(name='학생')
        instance.groups.add(default_group)
