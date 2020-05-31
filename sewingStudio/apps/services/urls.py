from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('price/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('portfolio/', views.portfolio, name='portfolio')

]
