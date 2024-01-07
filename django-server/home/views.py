from django.shortcuts import render, redirect
from .models import Calendar
from datetime import timedelta

def main(request):
    if request.method == 'POST':
        calendar = Calendar()
        calendar.author = request.user
        calendar.title = request.POST['eventTitle']
        calendar.label = request.POST['eventLabel']
        calendar.startdate = request.POST['eventStartDate']
        calendar.enddate = request.POST['eventEndDate']
        calendar.save()
        return redirect('home')
    cal = Calendar.objects.filter(author=request.user) if request.user.is_authenticated else None
    for c in cal:
        c.enddate = c.enddate+timedelta(days=1)
        if c.label == '강의':
            c.label='blue'
        elif c.label == '복습':
            c.label = 'green'
        elif c.label == '휴가':
            c.label = 'red'
    return render(request, './home/main.html', {'cal': cal})


def faq(request):
    return render(request, './home/faq.html')
