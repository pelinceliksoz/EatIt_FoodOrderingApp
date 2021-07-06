from django.urls import path
from . import views

urlpatterns = [
    path('search_restaurant', views.SearchRestaurant.as_view(), name='search_restaurant'),
    path('see_comments/<int:pk>/', views.SeeCommentsView.as_view(), name='see_comments'),
    path('main_page/', views.main_page_view, name='main_page'),
    path('show_orders/', views.show_orders, name='show_orders')


]