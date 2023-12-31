from django.shortcuts import render
from .models import Test
from lecture.models import Lecture
from chat.models import Message
from pathlib import Path
from threading import Thread
import sys
big = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(big))
from ai import evalbot
# Create your views here.


def evaluation(request, lecture_name):
    if request.method == 'POST':
        lecture_id = request.POST['lecture_id']

        # 채팅 메시지 기록
        chat_messages = Message.objects.filter(lecture_id = lecture_id).values_list('user_message','bot_message')
        chat_message = ', '.join(item for message in chat_messages for item in message)

        # 문제지 & 정답지
        lecture = Lecture.objects.get(id = lecture_id)
        video = lecture.video        
        statements = Test.objects.filter(video=video)
        

        eval_results = [[0, 0, 0, 0] for i in range(len(statements))]

        threads = []
        for idx, q in enumerate(statements):
            threads.append(Thread(target=evalbot.test_eval, args=(q.question, q.answer, eval_results, idx, chat_message)))

        for th in threads: th.start()
        for th in threads: th.join()

        for er in eval_results:
            print('문제:', er[0], '답:', er[1], '풀이:', er[2], '정답 여부:', er[3])
        checklist = [er[3] for er in eval_results]
        
        context = {
            'lecture_name': lecture_name,
            'num_correct': checklist.count('1'),
            'num_wrong': checklist.count('0'),
            'checklist': checklist,
        }
    else:
        context = {
            'lecture_name': lecture_name,
        }
    return render(request, "./evaluation/ev.html", context=context)