from django.shortcuts import render
from .models import Lecture


def index(request):

    lectures = Lecture.objects.order_by('-student_count')
    context = {
        'lectures': lectures,
    }

    return render(request, './home/index.html', context)
