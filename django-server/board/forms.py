from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(label='제목') # 위젯으로 바뀔 때 input 타입 텍스트로 바뀜, 기본 위젯
    body = forms.CharField(label='내용', widget=forms.Textarea) # 위젯 변경 설정
    
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']