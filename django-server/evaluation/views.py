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
        score, correct_count, wrong_count = 0, 0, 0
        explanations = []
        for er in eval_results:
            print(*map(': '.join, zip(["문제", "답", "풀이", "점수 및 보완할 부분"], er)))
            idx = er[3].find(':')
            point, explain = er[3][:idx], er[3][idx+1:]
            explanations.append(explain)
            # gpt가 다른 대답 뱉으면 문제 생길 소지 있음.
            point = int(point)
            if point >= 70: correct_count += 1
            else: wrong_count += 1
            score += point
        score //= len(eval_results)
        
        # Database 저장
        instance = TestResult(score)
        # 데이터베이스에 저장
        instance.save()

        context = {
            'lecture_name': lecture_name,
            'video_name': video_name,
            'num_correct': correct_count,
            'num_wrong': wrong_count,
            'checklist': explanations,
        }
    else:
        context = {
            'lecture_name': lecture_name,
        }
    return render(request, "./evaluation/page.html", context=context)
