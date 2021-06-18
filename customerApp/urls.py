from django.urls import path
from . import views

urlpatterns = [
    path('customerMainPage', views.CustomerMainPage.as_view(), name='customerMainPage'),
]