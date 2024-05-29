from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def mona_lisa(request):
    return HttpResponse("Страница монылызы, больше инфы тут нет, но представим что я вернул html")


def starry_night(request):
    return HttpResponse("Страница какой то ночи, я опять же не прикрепил никаких фотографий..")