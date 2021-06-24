from django.urls import path
from . import views

urlpatterns = [
    path('search_restaurant', views.searchRestaurant, name='search_restaurant'),
    path('see_comments/<int:pk>/', views.SeeComments.as_view(), name='see_comments'),


]