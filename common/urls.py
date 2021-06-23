from django.urls import path
from . import views

urlpatterns = [
    path('search_restaurant', views.searchRestaurant, name='search_restaurant'),


]