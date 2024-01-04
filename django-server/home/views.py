from django.shortcuts import render, redirect
from django.contrib import messages
from lecture.models import Lecture, Video
from accounts.models import UserMessage
from .models import Calendar
from .forms import CalendarModelForm


def index(request):
    if request.user.is_authenticated:
        # 사용자에게 미확인 메시지가 있는지 확인
        unread_messages = UserMessage.objects.filter(
            user=request.user, is_read=False)
        if unread_messages.exists():

            for unread_message in unread_messages:
                messages.info(request, unread_message.message, extra_tags=unread_message.sender)

    subject = request.GET.get('subject')

    lectures = Lecture.objects.filter(
        subject=subject) if subject else Lecture.objects.all()
    lectures = lectures.order_by('-student_count')
    for lecture in lectures:
        videos = Video.objects.filter(lecture=lecture)
        for video in videos:
            lecture.remain_time += video.video_duration
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
    return render(request, './home/Fullcalendar.html', {'form': form})
