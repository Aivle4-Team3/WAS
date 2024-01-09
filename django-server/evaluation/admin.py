from django.contrib import admin
from .models import TestPaper

# Register your models here.

class TestPaperAdmin(admin.ModelAdmin):
    list_display = ('question', 'video')

admin.site.register(TestPaper, TestPaperAdmin)
