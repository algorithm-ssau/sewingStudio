from django.shortcuts import render
from .models import Service, SubServices


def index(request):
    return render(request, 'index')