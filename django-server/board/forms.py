from django import forms
from .models import Post, Comment
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.Form):
    title = forms.CharField(label='제목')  # 위젯으로 바뀔 때 input 타입 텍스트로 바뀜, 기본 위젯
    body = forms.CharField(widget=CKEditorWidget())


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        labels = {
            'title': '제목',
            'body': '내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', ]
