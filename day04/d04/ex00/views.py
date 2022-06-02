from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'ex00/index.html')


def home(request):
    return HttpResponse("Piscine Django day04.")