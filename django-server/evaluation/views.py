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

    checklist = []
    for my, q in zip(a, qs):
        is_answer = evalbot.test_eval(my, q.answer)
        print('채점 결과: ', is_answer)
        checklist.append(is_answer)
    #시험 문제를 가져오기 -> 어느 비디오에서 왔는가? 
    #시험 문제를 풀게하기
    #채점까지 해야함.
    #채점 결과
    context = {
        'num_correct': checklist.count('1'),
        'num_wrong': checklist.count('0'),
        'checklist': checklist,
    }

    return render(request, "./evaluation/ev.html", context=context)