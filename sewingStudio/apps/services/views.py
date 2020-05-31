from django.http import HttpResponse
from django.shortcuts import render

from sewingStudio.apps.services.models import Service


def index(request):
    return render(request, 'landing/index.html')


def services(request):
    service_list = Service.objects.all()
    return render(request, 'service/prices.html', {'service_list': service_list})


def contacts(request):
    return render(request, 'landing/contacts.html')


def portfolio(request):
    return render(request, 'landing/portfolio.html')