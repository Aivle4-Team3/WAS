from accounts.models import UserMessage
from django.contrib import messages


class MessageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 요청을 처리하는 코드
        
        if request.user.is_authenticated:
            # 사용자에게 미확인 메시지가 있는지 확인
            unread_messages = UserMessage.objects.filter(
                user=request.user, is_read=False)
            if unread_messages.exists():

                for unread_message in unread_messages:
                    messages.info(request, unread_message.message, extra_tags=unread_message.sender)


        response = self.get_response(request)
        # 응답을 처리하는 코드
        return response
