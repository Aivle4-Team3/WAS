from django.shortcuts import render
from itertools import chain
from .models import Message
# Create your views here.


def chatpage(request, lecture_name):
    lecture_id = request.POST['lecture_id'] if request.method == 'POST' else None
    messages = Message.objects.filter(lecture_id=lecture_id)

    history = [[{'type': 'user', 'message': message.user_message, 'time': ''},
                {'type': 'bot',  'message': message.bot_message,  'time': ''}] for message in messages]
    history = list(chain(*history))

    context = {
        'lecture_name': lecture_name,
        'lecture_id': lecture_id,
        'history': history,
    }
    return render(request, "./chat/page.html", context)
