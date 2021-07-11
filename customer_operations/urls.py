from django.urls import path
from . import views

urlpatterns = [
    path('customer_main_page', views.CustomerMainPageView.as_view(), name='customer_main_page'),
    path('food_details/<int:pk>/', views.FoodDetailsView.as_view(), name='food_details'),
    path('make_comment/<int:pk>/', views.MakeCommentView.as_view(), name='make_comment'),
    path('like/<int:pk>/', views.LikeView.as_view(), name='like_food'),
    path('liked_foods', views.LikedFoodsView.as_view(), name='liked_foods'),
    path('remove_like/<int:pk>/', views.RemoveLikeView.as_view(), name='remove_like'),
    path('remove_comment/<int:pk>/', views.RemoveCommentView.as_view(), name='remove_comment'),
    path('remove_order/<int:pk>/', views.RemoveOrderView.as_view(), name='remove_order'),
    path('make_order/<int:pk>/', views.MakeOrderView.as_view(), name='make_order'),
    path('customer_own_orders', views.ShowCustomerOwnOrdersView.as_view(), name='customer_own_orders'),
    path('remove_order_customer/<int:pk>/', views.RemoveOrderCustomerView.as_view(), name='remove_order_customer'),
    path('other_customers_profile/<int:pk>/', views.OtherCustomersProfileView.as_view(), name='other_customers_profile'),
    path('cheapest_foods', views.CheapestFoodsView.as_view(), name='cheapest_foods'),
    path('popular_restaurants', views.PopularRestaurantsView.as_view(), name='popular_restaurants'),
    path('popular_foods', views.PopularFoodsView.as_view(), name='popular_foods'),
    path('cheapest_restaurants', views.CheapestRestaurantsView.as_view(), name='cheapest_restaurants'),
    path('most_liked_foods', views.MostLikedFoodsView.as_view(), name='most_liked_foods'),

]