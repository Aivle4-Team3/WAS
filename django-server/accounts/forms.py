from django import forms
from allauth.account.forms import SignupForm
from .models import User


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    website_url = forms.URLField(required=False)
    avatar = forms.ImageField(required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
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
