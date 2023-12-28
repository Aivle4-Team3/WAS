from django.shortcuts import render
from .models import Video
from home.models import Lecture

# Create your views here.


def lecture(request, id):
    context = {
        'video_file': Video.objects.get(id=id).file,
    }

    return render(request, './lecture/index.html', context)
