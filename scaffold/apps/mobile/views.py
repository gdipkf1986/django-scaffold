__author__ = 'Jovi'

from django.shortcuts import HttpResponse, render


def index(request):
    return render(request, 'mobile/index.html')
