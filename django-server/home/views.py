from django.shortcuts import render
from .models import Lecture


def index(request):

    lectures = Lecture.objects.order_by('-visited')
    context = {
        'lectures': lectures,
    }

    return render(request, './home/index.html', context)
