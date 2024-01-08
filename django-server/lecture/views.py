from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Lecture, Video
from datetime import timedelta
# Create your views here.

def showcase(request):
    subject = request.GET.get('subject')

    lectures = Lecture.objects.filter(
        subject=subject) if subject else Lecture.objects.all()
    lectures = lectures.order_by('-student_count')
    for lecture in lectures:
        videos = Video.objects.filter(lecture=lecture)
        for video in videos:
            lecture.remain_time += video.video_duration
    context = {
        'lectures': lectures,
    }

    return render(request, './lecture/showcase.html', context)


def room(request, lecture_name):
    if request.method == "POST":
        lecture = Lecture.objects.get(id=request.POST['lecture_id'])
        videos = lecture.videos.all()

        context = {
            'lecture': lecture,
            'videos': videos,
            'video_count': len(videos)
        }
        return render(request, './lecture/room.html', context)


@require_http_methods(["POST"])
def save_playback(request):
    pass
