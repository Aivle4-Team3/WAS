import sys, json
from channels.generic.websocket import WebsocketConsumer
from pathlib import Path
big = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(big))
from ai import chatbot


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

        self.send(text_data=json.dumps({"message": answer}))
