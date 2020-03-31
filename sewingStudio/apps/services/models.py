from django.db import models


class Service(models.Model):
    service_name = models.CharField('название услуги', max_length=100)
    service_description = models.TextField('описание услуги')
    service_price = models.FloatField('цена услуги')


class SubServices(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_service_name = models.CharField('название под-услуги', max_length=100)
    sub_service_description = models.TextField('описание под-услуги')
    sub_service_price = models.FloatField('цена под-услуги')
