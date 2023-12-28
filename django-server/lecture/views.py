from django.shortcuts import render
from .models import Video
# Create your views here.


def lecture(request, lecture_name):

    if request.method == "POST":
        context = {
            'video_file': Video.objects.get(id=request.POST['video_id']).file,
        }

        return render(request, './lecture/index.html', context)
