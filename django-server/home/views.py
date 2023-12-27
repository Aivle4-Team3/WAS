from django.shortcuts import render
from .models import Lecture


def index(request):

    lectures = Lecture.objects.order_by('-visited')
    context = {
        'lectures': lectures,
        'phrase_list': [
            "반복은 천재를 낳고, 믿음은 기적을 낳는다. － 안진수",
            "거인의 어깨에 올라서서 더 넓은 세상을 바라보라 － 지병규"
        ],
    }

    return render(request, './home/index.html', context)
