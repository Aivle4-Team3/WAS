import json
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime
from lecture.models import Video
from .models import Message
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

        # 데이터베이스에 저장
        video_id = self.scope['url_route']['kwargs']['room_name']
        video = Video.objects.get(id=video_id)
        instance = Message(
            video=video, user_message=message, bot_message=answer, user_time=message_time, bot_time=answer_time,
            user_message_embedded=chatbot.get_embedding(message), bot_message_embedded=chatbot.get_embedding(answer))
        instance.save()

        self.send(text_data=json.dumps({"message": answer}))
