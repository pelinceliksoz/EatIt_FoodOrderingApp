from django.urls import path, include
from . import views


urlpatterns = [
    path('restaurantMainPage', views.RestaurantMainPage.as_view(), name='restaurantMainPage'),
    path('addFood/<int:restaurant_id>/', views.AddFood.as_view(), name='addFood'),
    path('restaurantMenu/<int:pk>/', views.RestaurantMenu.as_view(), name='restaurantMenu'),
]