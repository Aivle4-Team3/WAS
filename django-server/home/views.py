from django.shortcuts import render, redirect
from lecture.models import Lecture
from .models import Calendar
from .forms import CalendarModelForm


def index(request):

    lectures = Lecture.objects.order_by('-student_count')
    context = {
        'lectures': lectures,
    }

    return render(request, './home/index.html', context)

def realhome(request):
    if request.method == 'POST':
        calendar = Calendar()
        calendar.author = request.user
        calendar.title = request.POST['eventTitle']
        calendar.label = request.POST['eventLabel']
        calendar.startdate = request.POST['eventStartDate']
        calendar.enddate = request.POST['eventEndDate']
        calendar.save()
        return redirect('realhome')
    
    return render(request, './home/Fullcalendar.html')
    # return render(request, './home/fullcalendar.html')

def calpark(request):
    if request.method == 'POST':
        form = CalendarModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('realhome')
    else:
        form = CalendarModelForm()
    return render(request, './home/Fullcalendar.html',{'form':form})
