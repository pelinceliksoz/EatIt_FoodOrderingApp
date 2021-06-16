from django.urls import path
from . import views

urlpatterns = [
    path('customerApp/customerMainPage', views.customerMainPage, name = 'customerMainPage'),
]