from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_countries import countries
from allauth.account.views import SignupView
from .models import User, UserMessage
from .forms import UserForm, CustomSignupForm
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse


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
    return render(request, './home/faq.html')


def consent(request):
    return render(request, 'account/consent.html')


@login_required
def delete(request):
    if request.method == 'POST':
        user = request.user
        user.delete()

    return HttpResponseRedirect(reverse('frontdoor'))


# 알림 메시지 삭제 - ajax 통신
@require_http_methods(["POST"])
def read_message(request):
    read_all = request.POST.get('read_all')
    id = request.POST.get('id')

    if read_all:
        for user in UserMessage.objects.all():
            user.is_read = True
            user.save()
    else:
        user = UserMessage.objects.get(id=id)
        user.is_read = True
        user.save()

    return JsonResponse({'result': 'success'})
