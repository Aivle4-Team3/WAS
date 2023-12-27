from django.shortcuts import render

# Create your views here.


def evaluation(request):
    return render(request, "./evaluation/ev.html")