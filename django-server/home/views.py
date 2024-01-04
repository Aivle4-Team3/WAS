from django.shortcuts import render, redirect
from lecture.models import Lecture
from .forms import CalendarModelForm


def index(request):

    lectures = Lecture.objects.order_by('-student_count')
    context = {
        'lectures': lectures,
    }

    return render(request, './home/index.html', context)

def realhome(request):

    return render(request, './home/fullcalendar.html')

def calpark(request):
    if request.method == 'POST':
        form = CalendarModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('realhome')
    else:
        form = CalendarModelForm()
    return render(request, './home/Fullcalendar.html',{'form':form})
