from django.shortcuts import render
from .models import Test
from lecture.models import Lecture
from chat.models import Message
from threading import Thread
from config.settings import chatbot

# Create your views here.


def evaluation(request, lecture_name):
    if request.method == 'POST':
        lecture_id = request.POST['lecture_id']

        # 채팅 메시지 기록
        chat_messages = Message.objects.filter(
            lecture_id=lecture_id).values_list('user_message', 'bot_message')

        # 문제지 & 정답지
        lecture = Lecture.objects.get(id=lecture_id)
        video = lecture.video
        statements = Test.objects.filter(video=video)

        # 결과 저장할 가변 리스트
        eval_results = [[0, 0, 0, 0] for i in range(len(statements))]

        # 쓰레딩
        threads = []
        for eval_result, statement in zip(eval_results, statements):
            threads.append(Thread(target=chatbot.eval_test, args=(
                statement.question, statement.answer, chatbot.test(chat_messages), eval_result)))

        for th in threads:
            th.start()
        for th in threads:
            th.join()

        # 결과
        for er in eval_results:
            print(*map(': '.join, zip(["문제", "답", "풀이", "정답 여부"], er)))
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
