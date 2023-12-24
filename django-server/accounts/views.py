from django.shortcuts import render
from django.forms.models import model_to_dict
from . import models


def login_success(request):
    return render(request, './account/login_success.html')


def mypage(request):
    # 접근 유저
    username = request.user
    # 접근 유저의 모델 읽기
    model = models.User.objects.get(username=username)

    if request.method == "POST":

        # 추가 데이터
        print(request.POST)
        # 추가 데이터 수정
        model.first_name = request.POST['firstName']
        model.last_name = request.POST['lastName']
        model.email = request.POST['email']
        model.organization = request.POST['organization']
        model.phoneNumber = request.POST['phoneNumber']

        # 접근 유저의 모델 저장
        model.save()

    context = {
        'profile': model_to_dict(model),
    }
    return render(request, './account/mypage.html', context=context)
