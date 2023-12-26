from django.shortcuts import render


def frontdoor(request):
    context = {
        # 배경 동영상
        'background_video': "https://www.youtube.com/embed/Ga-UF1j7cQ4?mute=1&amp;loop=1&amp;autoplay=1&amp;rel=0&amp;controls=0&amp;showinfo=0",
    }

    return render(request, './frontdoor/index.html', context)
