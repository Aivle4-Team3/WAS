from django.shortcuts import render
from .models import Message
# Create your views here.


def chatpage(request, lecture_name, video_name):
    video_id = request.POST['video_id'] if request.method == 'POST' else None
    messages = Message.objects.filter(video_id=video_id)

    history = [[{'type': 'user', 'message': message.user_message, 'time': message.user_time},
                {'type': 'bot',  'message': message.bot_message,  'time': message.bot_time}] for message in messages]

    context = {
        'lecture_name': lecture_name,
        'video_name': video_name,
        'video_id': video_id,
        'history': history,
    }
    return render(request, "./chat/page.html", context)
