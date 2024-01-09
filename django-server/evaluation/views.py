import re
import json
from django.shortcuts import render
from .models import TestResult
from threading import Thread
from config.settings import chatbot
from accounts.models import User
from lecture.models import Video
from chat.models import Message
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.


def evaluation(request, lecture_name, video_name):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user = User.objects.get(id=user_id)
        video_id = request.POST['video_id']
        video = Video.objects.get(id=video_id)

        # 메시지검색
        chat_messages = Message.objects.filter(user=user_id, video=video_id)

        # 문제지 & 정답지
        statements = Video.objects.get(id=video_id).testpapers.all()

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
        scores = []
        for er in eval_results:
            print(*map(': '.join, zip(["문제", "답", "풀이", "점수 및 보완할 부분"], er)), sep='\n')
            idx = er[3].find(':')
            point, explain = er[3][:idx], er[3][idx+1:]
            explanations.append(explain)
            # gpt가 다른 대답 뱉으면 문제 생길 소지 있음.
            point = int(point)
            scores.append(point)

        score = sum(scores)/len(scores)*100
        correct_count = sum(1 for score in scores if score >= 70)
        wrong_count = len(scores) - correct_count

        # TestResult 평가지당 개별 점수로 저장
        for testpaper, score in zip(statements, scores):
            instance = TestResult(user=user, video=video, score=score)
            # 데이터베이스에 저장
            instance.save()

        # 이번 평가의 점수와 설명
        evals = [{'score': score, 'explation': explation}
                 for score, explation in zip(scores, explanations)]

        # 유저당 점수의 기록
        test_results = TestResult.objects.filter(user=user, video=video)
        fields_data = [{'evaluation_date': obj.evaluation_date,
                        'score': obj.score} for obj in test_results]
        json_result = json.dumps(fields_data, cls=DjangoJSONEncoder)

        context = {
            'score': score,
            'lecture_name': lecture_name,
            'video_name': video_name,
            'num_correct': correct_count,
            'num_wrong': wrong_count,
            'detail_evals': evals,
            'history_evals': json_result,
        }
    else:
        context = {
            'lecture_name': lecture_name,
        }
    return render(request, "./evaluation/page.html", context=context)
