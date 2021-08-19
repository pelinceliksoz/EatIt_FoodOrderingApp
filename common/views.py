import numpy
from django.shortcuts import render,redirect
from django.views import View
from .models import Comment, Food, Restaurant, Customer
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import get_user_type

# import pandas as pd
# import numpy as np
# import matplotlib
# from matplotlib import pyplot as plt
# import sklearn
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.cluster import KMeans
# import pickle
# import sys
# import ast
#
# print("************************************************************************")
# customers = Customer.objects.filter().values_list('pk', flat=True)
# customers_array = numpy.array(customers)
# print(customers_array)
# categories = Food.CATEGORY
# i = 0
# categories_array = []
# while i < 9:
#     categories_array.append(categories[i][1])
#     i = i+1
# numpy.array(categories_array)
# print(categories_array)
# category_count_customers = []
# for customer in customers_array:
#     category_count_array = []
#     for category in categories_array:
#         foods = Food.objects.filter(likes__user=customer, category=category)
#         foods_array = numpy.array(foods)
#         category_count_array.append(foods_array.size)
#     numpy.array(category_count_array)
#     foods_array = numpy.array(foods)
#     category_count_customers.append(category_count_array)
#     numpy.array(category_count_customers)
# print(category_count_customers)
# print("************************************************************************")
#
# kmeans = KMeans(n_clusters=3, random_state=0).fit(category_count_customers)
# print(kmeans.predict([category_count_customers[1]]))
# print(kmeans.labels_)
#
# print("----------------------------------------------------------------------")
#
#


class SearchRestaurant(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        if get_user_type(request.user.id) == 1:
            searched = request.POST['searched']
            foods = Food.objects.filter(food_name__icontains=searched)
            context = {
                'searched': searched,
                'foods': foods,
                'user': user
            }
            return render(request, 'common/search_food.html', context)
        else:
            searched = request.POST['searched']
            restaurants = Restaurant.objects.filter(restaurant_name__icontains=searched)
            context = {
                'user': user,
                'searched': searched,
                'restaurants': restaurants
            }
            return render(request, 'common/search_restaurant.html', context)


class SearchFood(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context = {
            'user': user
        }
        return render(request, 'common/search_food.html', context)

    def post(self, request):
        context = {}
        return render(request, 'common/search_food.html', context)


class SeeCommentsView(LoginRequiredMixin, View):
    def get(self, request, pk):
        food = Food.objects.get(pk=pk)
        comments = Comment.objects.filter(food=food)
        context = {
            'comments': comments
        }
        return render(request, 'common/see_comments.html', context)


def main_page_view(request):
    uid = request.user.id
    if get_user_type(uid) == 1:
        return redirect('restaurant_main_page')
    else:
        return redirect('customer_main_page')


def show_orders(request):
    uid = request.user.id
    if get_user_type(uid) == 1:
        return redirect('restaurant_show_orders')
    else:
        return redirect('customer_own_orders')







