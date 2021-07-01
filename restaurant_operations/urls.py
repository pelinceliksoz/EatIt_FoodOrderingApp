from django.urls import path, include
from . import views


urlpatterns = [
    path('restaurant_main_page', views.RestaurantMainPageView.as_view(), name='restaurant_main_page'),
    path('add_food/<int:restaurant_id>/', views.AddFoodView.as_view(), name='add_food'),
    path('restaurant_menu/<int:pk>/', views.RestaurantMenuView.as_view(), name='restaurant_menu'),
    path('update_food/<int:pk>/', views.UpdateFoodView.as_view(), name='update_food'),
    path('delete_food/<int:pk>/', views.DeleteFoodView.as_view(), name='delete_food'),
    path('restaurant_show_orders', views.RestaurantShowOrdersView.as_view(), name='restaurant_show_orders'),

]