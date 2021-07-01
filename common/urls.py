from django.urls import path
from . import views

urlpatterns = [
    path('search_restaurant', views.SearchRestaurant.as_view(), name='search_restaurant'),
    path('see_comments/<int:pk>/', views.SeeCommentsView.as_view(), name='see_comments'),


]