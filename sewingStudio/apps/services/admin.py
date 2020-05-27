from django.contrib import admin

from sewingStudio.apps.services.models import Service, SubServices
# Register your models here.

admin.site.register(Service)
admin.site.register(SubServices)