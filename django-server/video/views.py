from django.shortcuts import render
from .models import Video

# Create your views here.


def video(request, video_name):

    context = {
        'video_file': Video.objects.get(name=video_name).file,
        }

    return render(request, './video/index.html', context)