from django.contrib import admin
from .models import Message

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'user_message', 'bot_message')

admin.site.register(Message, MessageAdmin)
