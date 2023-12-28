from django.shortcuts import render
from .models import Lecture
# Create your views here.


def lecture(request, lecture_name):

    if request.method == "POST":

        lecture = Lecture.objects.get(id=request.POST['lecture_id'])

        context = {
            'lecture': lecture,
        }

        return render(request, './lecture/index.html', context)
