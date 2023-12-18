from django.shortcuts import render

# Create your views here.

def chatpage(request):

    context = {
        'chatbot': "https://f55981e5b3327c9ca8.gradio.live/",
        }

    return render(request, './chat/index.html', context)