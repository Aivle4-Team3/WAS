from django.shortcuts import render

# Create your views here.


def chatpage(request, lecture_name, video_name):
    video_id = request.POST['video_id'] if request.method == 'POST' else None

    context = {
        'lecture_name': lecture_name,
        'video_name': video_name,
        'video_id': video_id,
    }
    return render(request, "./chat/page.html", context)
