from django.shortcuts import render
from .models import Message
from lecture.models import Enrollment
from accounts.models import User
# Create your views here.


def chat(request, lecture_name, video_name):
    # user, video id를 POST로 전송 받음
    user_id = request.POST['user_id'] if request.method == 'POST' else None
    video_id = request.POST['video_id'] if request.method == 'POST' else None
    user = User.objects.get(id=user_id)

    # 관계 생성
    enrollment, created = Enrollment.objects.get_or_create(user_id=user_id, video_id=video_id)
    # 메시지검색
    messages = Message.objects.filter(enrollment=enrollment)

    # 기록 읽기
    history = [[{'type': 'user', 'message': message.user_message, 'time': message.user_time},
                {'type': 'bot',  'message': message.bot_message,  'time': message.bot_time}] for message in messages]

    context = {
        'lecture_name': lecture_name,
        'video_name': video_name,
        'video_id': video_id,
        'user': user,
        'history': history,
    }
    return render(request, "./chat/page.html", context)
