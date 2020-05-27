from django.shortcuts import render

from sewingStudio.apps.services.models import Service

def index(request):
    service_list = Service.objects.all()
    return render(request, 'service/list.html', {'service_list': service_list})
