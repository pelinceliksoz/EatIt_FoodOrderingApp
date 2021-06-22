from django.urls import path
from . import views

urlpatterns = [
    path('customer_main_page', views.CustomerMainPage.as_view(), name='customer_main_page'),
    path('order_food/<int:pk>/', views.OrderFood.as_view(), name='order_food'),
    path('make_comment/<int:pk>/', views.MakeComment.as_view(), name='make_comment'),
    path('like/<int:pk>/', views.LikeView.as_view(), name='like_food'),
    path('liked_foods', views.LikedFoods.as_view(), name='liked_foods'),
    path('remove_like/<int:pk>/', views.RemoveLike.as_view(), name='remove_like')
]