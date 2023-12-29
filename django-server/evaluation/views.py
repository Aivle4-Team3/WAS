from django.shortcuts import render
from .models import Test
from pathlib import Path
import sys
big = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(big))
from ai import testbot, evalbot
# Create your views here.


def evaluation(request):
    return render(request, "./evaluation/ev.html", context={})

def evaluation1(request, video1):
    a = []
    qs = Test.objects.filter(video=video1)
    for q in qs:
        t = testbot.test_ai(q.question)
        a.append(t)
        print("답: ",t)
    for my, q in zip(a, qs):
        print('채점 결과: ', evalbot.test_eval(my, q.answer))
    #시험 문제를 가져오기 -> 어느 비디오에서 왔는가? 
    #시험 문제를 풀게하기
    #채점까지 해야함.
    #채점 결과
    return render(request, "./evaluation/ev.html", context={})