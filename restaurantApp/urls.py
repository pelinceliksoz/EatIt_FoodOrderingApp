from django.urls import path, include
from . import views


urlpatterns = [
    path('restaurantMainPage', views.restaurant_main_page, name='restaurantMainPage'),
    path('addFood/<int:restaurant_id>/', views.AddFood.as_view(), name='addFood'),
    path('restaurantMenu', views.restaurant_menu, name='restaurantMenu'),
]