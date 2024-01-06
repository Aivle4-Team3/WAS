from accounts.models import UserMessage
from django.contrib import messages

# 어디서든 메시지 확인
class MessageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 승인된 사용자
        if request.user.is_authenticated:
            unread_messages = UserMessage.objects.filter(user=request.user, is_read=False)
            # 사용자에게 미확인 메시지가 있는지 확인
            if unread_messages.exists():

                # Django의 내장 메시징 프레임워크에 등록
                for unread_message in unread_messages:
                    messages.info(request, unread_message)

        response = self.get_response(request)
        return response
