from django.urls import path
from . import views

urlpatterns = [
    path('restaurantApp/restaurantMainPage', views.restaurantMainPage, name = 'restaurantMainPage'),
]