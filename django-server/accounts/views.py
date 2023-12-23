from django.shortcuts import render


def login_success(request):
    return render(request, './account/login_success.html')


def mypage(request):
    return render(request, './account/mypage.html')
