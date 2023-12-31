import sys
import json
from channels.generic.websocket import WebsocketConsumer
from pathlib import Path
from lecture.models import Lecture
from .models import Message
from ai import chatbot

big = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(big))


class ChatConsumer(WebsocketConsumer):
    history = []

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        answer = chatbot.chat(message, self.history)

        print("query", message)
        print("answer", answer)

        # 데이터베이스에 저장
        lecture_id = self.scope['url_route']['kwargs']['room_name']
        lecture = Lecture.objects.get(id=lecture_id)
        instance = Message(
            lecture=lecture, user_message=message, bot_message=answer)
        instance.save()

        self.send(text_data=json.dumps({"message": answer}))
