from django.shortcuts import render
from .models import Video

# Create your views here.


def lecture(request, lecture_name):

    context = {
        'video_file': Video.objects.get(name=lecture_name).file,
    }

    return render(request, './lecture/index.html', context)
