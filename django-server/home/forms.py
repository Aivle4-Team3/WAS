from django import forms
from .models import Calendar
from ckeditor.widgets import CKEditorWidget


class CalendarModelForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['author','title', 'label', 'startdate','enddate']
