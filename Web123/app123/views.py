from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def Index(request):
    return render(request, 'login.html')


def Login(request):
    return render(request, 'login.html')