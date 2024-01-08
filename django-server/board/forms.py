from django import forms
from .models import *
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


class CommunityModelForm(PostModelForm):
    class Meta(PostModelForm.Meta):
        model = Community


class QnAModelForm(PostModelForm):
    class Meta(PostModelForm.Meta):
        model = QnA


class NoticeModelForm(PostModelForm):
    class Meta(PostModelForm.Meta):
        model = Notice


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', ]
