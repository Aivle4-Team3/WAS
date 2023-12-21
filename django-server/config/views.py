from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    context = {
        'background_video': "https://www.youtube.com/embed/Ga-UF1j7cQ4",
        }

    return render(request, './account/index.html', context)

def index(request):
    return HttpResponse("빈 페이지")