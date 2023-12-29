from django.shortcuts import render

# Create your views here.


def chatpage(request, lecture_name):
    context = {
        'lecture_name': lecture_name
    }
    return render(request, "./chat/page.html", context)
