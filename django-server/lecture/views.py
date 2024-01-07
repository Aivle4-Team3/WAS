from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Lecture, Video, Enrollment
from datetime import timedelta
# Create your views here.


def lecture(request, lecture_name):
    if request.method == "POST":
        lecture = Lecture.objects.get(id=request.POST['lecture_id'])
        videos = lecture.videos.all()
        seconds = 0

        if request.user.enrollments.exists():
            enrollments = [video.enrollments.get(user=request.user) for video in videos]

            times = map(lambda enrollment: enrollment.playback_duration, enrollments)
            seconds = list(map(lambda duration: duration.total_seconds(), times))

            for video, second in zip(videos, seconds):
                video.second = second

            for video in videos:
                lecture.remain_time += video.video_duration

        context = {
            'lecture': lecture,
            'videos': videos,
            'seconds': seconds,
            'video_count': len(videos)
        }
        return render(request, './lecture/index.html', context)


@require_http_methods(["POST"])
def save_playback(request):
    # 재생한 시간 전송 받음
    seconds = float(request.POST.get('seconds', 0))
    time = timedelta(seconds=seconds)

    video_id = request.POST.get('video_id')
    video = Video.objects.get(id=video_id)
    enrollment = Enrollment.objects.get(user=request.user, video=video)

    # 재생한 시간 저장
    enrollment.playback_duration = time
    enrollment.save()

    return JsonResponse({'result': 'success'})
