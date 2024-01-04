from django.shortcuts import render
from .models import Lecture, Video
# Create your views here.



def lecture(request, lecture_name):

    if request.method == "POST":

        lecture = Lecture.objects.get(id=request.POST['lecture_id'])
        videos = Video.objects.select_related('lecture').filter(lecture_id=lecture.id)

        for video in videos:
            lecture.remain_time += video.video_duration
        context = {
            'lecture': lecture,
            'videos': videos,
        }
        return render(request, './lecture/index.html', context)
