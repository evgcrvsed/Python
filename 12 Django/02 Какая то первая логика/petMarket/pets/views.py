from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request, cat_id):
    return HttpResponse(f"Информация о питомце под id: {cat_id}")