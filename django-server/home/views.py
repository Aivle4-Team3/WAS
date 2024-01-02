from django.shortcuts import render
from lecture.models import Lecture


def index(request):

    lectures = Lecture.objects.order_by('-student_count')
    context = {
        'lectures': lectures,
    }

    return render(request, './home/index.html', context)

def realhome(request):

    return render(request, './home/fullcalendar.html')
