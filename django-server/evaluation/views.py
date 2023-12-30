from django.shortcuts import render
from .models import Test
from pathlib import Path
from threading import Thread
import sys
big = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(big))
from ai import evalbot
# Create your views here.


def evaluation(request):
    return render(request, "./evaluation/ev.html", context={})

def evaluation1(request, video1):
    qs = Test.objects.filter(video=video1)
    q_count = len(qs)
    eval_results = [[0, 0, 0, 0] for i in range(q_count)]

    threads = []
    for idx, q in enumerate(qs):
        threads.append(Thread(target=evalbot.test_eval, args=(q.question, q.answer, eval_results, idx)))

    for th in threads: th.start()
    for th in threads: th.join()

    for er in eval_results:
        print('문제:', er[0], '답:', er[1], '풀이:', er[2], '정답 여부:', er[3])
    return render(request, "./evaluation/ev.html", context={})