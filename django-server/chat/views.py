from django.shortcuts import render

# Create your views here.

def chatpage(request):

    context = {
        'chatbot': "https://6daac81fc44a48e78e.gradio.live",
        }

    return render(request, './chat/index.html', context)


def chatservice(request):
    return render(request, './chat/chat.html')

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})