from django.shortcuts import render


def login(request):
    context = {
        'background_video': "https://www.youtube.com/embed/Ga-UF1j7cQ4",
    }

    return render(request, './account/index.html', context)


def login_success(request):
    return render(request, './account/login_success.html')
