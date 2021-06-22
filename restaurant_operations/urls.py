from django.urls import path, include
from . import views


urlpatterns = [
    path('restaurant_main_page', views.RestaurantMainPage.as_view(), name='restaurant_main_page'),
    path('add_food/<int:restaurant_id>/', views.AddFood.as_view(), name='add_food'),
    path('restaurant_menu/<int:pk>/', views.RestaurantMenu.as_view(), name='restaurant_menu'),
    path('update_food/<int:pk>/', views.UpdateFood.as_view(), name='update_food'),
    path('delete_food/<int:pk>/', views.DeleteFood.as_view(), name='delete_food'),
]