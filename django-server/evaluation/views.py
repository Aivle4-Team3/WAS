from django.shortcuts import render
from lecture.models import Video
from chat.models import Message
from .models import TestResult
from threading import Thread
from config.settings import chatbot

# Create your views here.


def evaluation(request, lecture_name, video_name):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        video_id = request.POST['video_id']

        # 메시지검색
        chat_messages = Message.objects.filter(video=video_id)

        # 문제지 & 정답지
        statements = Video.objects.get(id=video_id).testpapers.all()
        # Video.objects.prefetch_related('testpapers').get(id=video_id).testpapers.all()

        # 결과 저장할 가변 리스트
        eval_results = [['', '', '', ''] for i in range(len(statements))]

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
            print(*map(': '.join, zip(["문제", "답", "풀이", "점수"], er)))
        checklist = [er[3] for er in eval_results]
        
        # Database 저장
        instance = TestResult(score)
        # 데이터베이스에 저장
        instance.save()

        context = {
            'lecture_name': lecture_name,
            'video_name': video_name,
            'num_correct': checklist.count('1'),
            'num_wrong': checklist.count('0'),
            'checklist': checklist,
        }
    else:
        context = {
            'lecture_name': lecture_name,
        }
    return render(request, "./evaluation/page.html", context=context)
