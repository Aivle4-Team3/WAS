from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, './account/login.html')

def index(request):
    return HttpResponse("빈 페이지")