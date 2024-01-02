from django import forms
from .models import Message

class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['lecture', 'user_message', 'bot_message', ]