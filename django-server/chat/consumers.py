import json
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime
from lecture.models import Video
from accounts.models import User
from .models import Message
from lecture.models import Enrollment
import urllib.parse
from config.settings import chatbot


class ChatConsumer(WebsocketConsumer):
    history = []

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        message_time = datetime.now()

        answer = chatbot.chat(message, self.history)
        answer_time = datetime.now()

        print("query", message)
        print("answer", answer)

        # 쿼리 문자열 파싱 /?key=value
        query_string = self.scope['query_string'].decode('utf8')
        params = urllib.parse.parse_qs(query_string)
        # 쿼리 파라미터 추출
        video_id = params.get('video_id', [None])[0]
        # 방 파라미터 추출
        user_id = self.scope['url_route']['kwargs']['room_name']

        # 참조 객체들
        video = Video.objects.get(id=video_id)
        user = User.objects.get(id=user_id)
        # 관계 연관
        enrollment = Enrollment.objects.get(user=user, video=video)

        # Message 생성
        instance = Message(
            user_message=message, bot_message=answer, user_time=message_time, bot_time=answer_time,
            user_message_embedded=chatbot.get_embedding(message), bot_message_embedded=chatbot.get_embedding(answer),
            enrollment=enrollment)
        # 데이터베이스에 저장
        instance.save()

        self.send(text_data=json.dumps({"message": answer}))
