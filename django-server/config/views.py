from django.shortcuts import render


def enterence(request):
    context = {
        'background_video': "https://www.youtube.com/embed/Ga-UF1j7cQ4",
    }

    return render(request, './enterence.html', context)


def login_success(request):
    return render(request, './account/login_success.html')
