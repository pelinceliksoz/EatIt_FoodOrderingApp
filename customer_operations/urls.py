from django.urls import path
from . import views

urlpatterns = [
    path('customer_main_page', views.CustomerMainPage.as_view(), name='customer_main_page'),
    path('food_details/<int:pk>/', views.FoodDetails.as_view(), name='food_details'),
    path('make_comment/<int:pk>/', views.MakeComment.as_view(), name='make_comment'),
    path('like/<int:pk>/', views.LikeView.as_view(), name='like_food'),
    path('liked_foods', views.LikedFoods.as_view(), name='liked_foods'),
    path('remove_like/<int:pk>/', views.RemoveLike.as_view(), name='remove_like'),
    path('remove_comment/<int:pk>/', views.RemoveComment.as_view(), name='remove_comment'),
    path('confirm_order_customer/<int:pk>/', views.ConfirmOrderCustomer.as_view(), name='confirm_order_customer'),
    path('customer_show_orders', views.CustomerShowOrders.as_view(), name='customer_show_orders'),
    path('remove_order/<int:pk>/', views.RemoveOrder.as_view(), name='remove_order'),

]