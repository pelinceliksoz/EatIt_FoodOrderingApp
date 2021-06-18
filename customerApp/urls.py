from django.urls import path
from . import views

urlpatterns = [
    path('customerMainPage', views.customerMainPage, name='customerMainPage'),
]