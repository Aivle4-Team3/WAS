from django.shortcuts import render
from .models import Test
from pathlib import Path
import sys
big = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(big))
from ai import testbot
# Create your views here.


def evaluation(request):
    return render(request, "./evaluation/ev.html", context={})

def evaluation1(request, video1):
    a = []
    print(video1)
    qs = Test.objects.filter(video=video1)
    for q in qs:
        a.append(testbot.test_ai(q.question))
    test_eval(my_ai_ans, true_ans)
    #시험 문제를 가져오기 -> 어느 비디오에서 왔는가? 
    #시험 문제를 풀게하기
    #채점까지 해야함.
    #채점 결과
    return render(request, "./evaluation/ev.html", context={})