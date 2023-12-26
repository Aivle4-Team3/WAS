from django.shortcuts import render


def frontdoor(request):
    context = {
        # 배경 동영상
        'background_video': "https://www.youtube.com/embed/Ga-UF1j7cQ4",
    }

    return render(request, './frontdoor/index.html', context)
