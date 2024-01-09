import io
import tempfile
import whisper
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.http import require_http_methods
from .models import Message
from accounts.models import User
from lecture.models import Video
# Create your views here.


@xframe_options_exempt
def chat(request, lecture_name, video_name):
    # user, video id를 POST로 전송 받음
    user_id = request.POST['user_id'] if request.method == 'POST' else None
    video_id = request.POST['video_id'] if request.method == 'POST' else None
    user = User.objects.get(id=user_id)
    video = Video.objects.get(id=video_id)

    # 메시지검색
    messages = Message.objects.filter(user=user, video=video)

    # 기록 읽기
    history = [[{'type': 'user', 'message': message.user_message, 'time': message.user_time},
                {'type': 'bot',  'message': message.bot_message,  'time': message.bot_time}] for message in messages]

    context = {
        'lecture_name': lecture_name,
        'video': video,
        'user': user,
        'history': history,
    }
    return render(request, "./chat/page.html", context)


@require_http_methods(["POST"])
def voice(request):
    audio_file = request.FILES['audioFile']
    audio_data = io.BytesIO(audio_file.read())

    # 임시 파일에 오디오 데이터를 쓰기
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
        tmp_file.write(audio_data.read())
        temp_file_path = tmp_file.name

    # 모델 로드 및 트랜스크립션 수행
    model = whisper.load_model("base")
    result = model.transcribe(temp_file_path)
    print(result["text"])
