from django import forms
from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from .models import User


# 기본 가입 폼 추가
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Placeholder Text'}))
    last_name = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = '이름'
        self.fields['last_name'].label = '성'
        self.fields['avatar'].label = '프로필 이미지'

        for key, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field.label })

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user


# 소셜로그인 후 가입 폼 추가
class CustomSocialSignupForm(SocialSignupForm):
    first_name = forms.CharField(required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'Placeholder Text'}))
    last_name = forms.CharField(required=False)
    avatar = forms.ImageField(required=False)

    def save(self, request):
        # user.additional_field = self.cleaned_data['additional_field']
        user = super(CustomSocialSignupForm, self).save(request)
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'organization', 'country', 'phone_number', 'avatar']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            # 리스트 목록의 필드들은 필수가 아님
            self.fields[field].required = False
