from django.shortcuts import render
from django_countries import countries
from allauth.account.views import SignupView
from .models import User
from .forms import UserForm, CustomSignupForm


class CustomSignupView(SignupView):
    form_class = CustomSignupForm


def mypage(request):
    # 접근 유저
    username = request.user
    # 접근 유저의 모델 읽기
    model = User.objects.get(username=username)

    if request.method == "POST":

        # 추가 폼 데이터
        print(request.POST)
        # 추가 파일 데이터
        print(request.FILES)

        # 모델폼으로 수정
        user_form = UserForm(request.POST, request.FILES, instance=model)

        # 유효성 검사 후 저장
        if user_form.is_valid():
            user_form.save()

    context = {'user': model, 'countries': countries}
    return render(request, './account/mypage.html', context=context)


def faq(request):
    # # 접근 유저
    # username = request.user
    # # 접근 유저의 모델 읽기
    # model = models.User.objects.get(username=username)

    # if request.method == "POST":

    #     # 추가 폼 데이터
    #     print(request.POST)
    #     # 추가 파일 데이터
    #     print(request.FILES)

    #     # 모델폼으로 수정
    #     user_form = UserForm(request.POST, request.FILES, instance=model)

    #     # 유효성 검사 후 저장
    #     if user_form.is_valid():
    #         user_form.save()

    # context = {'user': model, 'countries': countries}
    return render(request, './home/faq.html')
