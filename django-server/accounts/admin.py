from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):

    # admin 페이지에서 사용자 수정할때 입력폼
    fieldsets = UserAdmin.fieldsets + (
        (
            "추가 프로필",
            {
                "fields": ('organization', 'country', 'phone_number', 'avatar')
            },
        ),
    )


# Register your models here.
admin.site.register(User, CustomUserAdmin)
