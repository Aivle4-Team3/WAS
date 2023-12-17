from django.shortcuts import render

# Create your views here.

def chatpage(request):

    context = {
        'chatbot': "https://d2503e5b12ffcb1865.gradio.live/",
        }

    return render(request, './chat/index.html', context)