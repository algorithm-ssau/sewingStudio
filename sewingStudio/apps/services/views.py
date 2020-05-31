from django.http import HttpResponse
from django.shortcuts import render

from sewingStudio.apps.services.models import Service


def index(request):
    return render(request, 'landing/index.html')


def services(request):
    service_list = Service.objects.all()
    return render(request, 'service/list.html', {'service_list': service_list})
