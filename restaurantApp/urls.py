from django.urls import path, include
from . import views


urlpatterns = [
    path('restaurantMainPage', views.RestaurantMainPage.as_view(), name='restaurantMainPage'),
    path('addFood/<int:restaurant_id>/', views.AddFood.as_view(), name='addFood'),
    path('restaurantMenu/<int:pk>/', views.RestaurantMenu.as_view(), name='restaurantMenu'),
    path('updateFood/<int:pk>/', views.UpdateFood.as_view(), name='updateFood'),
    path('deleteFood/<int:pk>/', views.DeleteFood.as_view(), name='deleteFood'),
]