from django.shortcuts import render, redirect
from .models import Calendar


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
    return render(request, './home/main.html', {'cal': cal})


def faq(request):
    return render(request, './home/faq.html')
