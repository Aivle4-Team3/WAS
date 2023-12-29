from django.shortcuts import render
from .models import Test

# Create your views here.


def evaluation(request):
    #시험 문제를 가져오기 -> 어느 비디오에서 왔는가? 
    #시험 문제를 풀게하기
    #채점까지 해야함.
    #채점 결과
    return render(request, "./evaluation/ev.html", context={})

def evaluation1(request, video1):
    print(video1)
    qs = Test.objects.filter(video=video1)
    for q in qs:
        print(q.question)
    #시험 문제를 가져오기 -> 어느 비디오에서 왔는가? 
    #시험 문제를 풀게하기
    #채점까지 해야함.
    #채점 결과
    return render(request, "./evaluation/ev.html", context={})