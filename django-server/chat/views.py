from django.shortcuts import render

# Create your views here.


def chatpage(request, lecture_name):
    lecture_id = request.POST['lecture_id'] if request.method == 'POST' else None

    context = {
        'lecture_name': lecture_name,
        'lecture_id': lecture_id,
    }
    return render(request, "./chat/page.html", context)
