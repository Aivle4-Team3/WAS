from django.shortcuts import render
from .models import Lecture

def index(request):

    lectures = Lecture.objects.order_by('-title')
    context = {
        'lectures': lectures,
        }

    return render(request, './home/index.html', context)

def login(request):
    return render(request, './home/login.html')