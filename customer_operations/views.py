import numpy
import random
from django.contrib.contenttypes.fields import GenericRelation
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views import View
from common.models import Food, Comment, Order
from customer_operations.forms import MakeCommentForm, MakeOrderForm
from restaurant_operations.models import Restaurant
from customer_operations.models import Customer
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import get_user_type
from django.http import JsonResponse
from django.db.models import Avg, Max, Min

import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import pickle
import sys
import ast

print("************************************************************************")
customers = Customer.objects.filter().values_list('pk', flat=True)
customers_array = numpy.array(customers)
print(customers_array)
categories = Food.CATEGORY
i = 0
categories_array = []
while i < 9:
    categories_array.append(categories[i][1])
    i = i+1
numpy.array(categories_array)
print(categories_array)
category_count_customers = []
for customer in customers_array:
    category_count_array = []
    for category in categories_array:
        foods = Food.objects.filter(likes__user=customer, category=category)
        foods_array = numpy.array(foods)
        category_count_array.append(foods_array.size)
    numpy.array(category_count_array)
    foods_array = numpy.array(foods)
    category_count_customers.append(category_count_array)
    numpy.array(category_count_customers)
print(category_count_customers)
print("************************************************************************")

kmeans = KMeans(n_clusters=3, random_state=0).fit(category_count_customers)
print(kmeans.predict([category_count_customers[1]]))
print(kmeans.labels_)

print("----------------------------------------------------------------------")





class CustomerMainPageView(LoginRequiredMixin, View):
    def get(self, request):
        user_name = request.user.first_name
        all_restaurants = Restaurant.objects.all().order_by('restaurant_name')
        customer = request.user.customuser.customer
        context = {
            'customer': customer,
            'user_name': user_name,
            'all_restaurants': all_restaurants,
        }
        return render(request, 'customer_operations/customer_main_page.html', context)


class FoodDetailsView(LoginRequiredMixin, View):
    def get(self, request, pk):
        food = Food.objects.get(pk=pk)
        stuff = get_object_or_404(Food, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        print(stuff.id , request.user.id)
        print (stuff.likes, type(stuff.likes))
        if stuff.likes.filter(user__user_id=request.user.id).exists():
            liked = True

        order_form = MakeOrderForm()
        comment_form = MakeCommentForm()
        context = {
            'food': food,
            'total_likes': total_likes,
            'order_form': order_form,
            'comment_form': comment_form,
            'liked': liked,
        }
        return render(request, 'customer_operations/food_details.html', context)


class LikeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        customer = request.user.customuser.customer
        food_id = request.POST['food_id']
        food = get_object_or_404(Food, id=food_id)
        like_num = food.like_count
        print(food.likes.filter(user_id=request.user.customuser.customer.user_id).exists())
        if food.likes.filter(user_id=request.user.customuser.customer.user_id).exists():
            food.likes.remove(request.user.customuser.customer)
            like_num = like_num - 1
            liked = False
        else:
            food.likes.add(request.user.customuser.customer)
            liked = True
            like_num = like_num + 1
        food.like_count = like_num
        food.save()

        html = render_to_string(template_name='djangoP/like.html', context={'liked': liked})
        return JsonResponse({'liked': liked})


class LikedFoodsView(LoginRequiredMixin, View):
    def get(self, request):
        if get_user_type(request.user.id) == 1:
            restaurant = request.user.customuser.restaurant
            restaurant_foods = Food.objects.filter(restaurant=restaurant)
            comments = Comment.objects.filter(food__restaurant=restaurant)
            context = {
                'restaurant': restaurant,
                'restaurant_foods': restaurant_foods,
                'comments': comments
            }
            return render(request, 'restaurant_operations/restaurant_likes_comments.html', context)
        else:
            customer = request.user.customuser.customer
            liked_foods = Food.objects.filter(likes=customer)
            customer_comments = Comment.objects.filter(customer=customer)
            context = {
                'customer_comments': customer_comments,
                'customer_name': customer,
                'liked_foods': liked_foods
            }
            print(context)
            return render(request, 'customer_operations/liked_foods.html', context)


class RemoveLikeView(LoginRequiredMixin, View):
    def get(self, request, pk):
        food = Food.objects.get(id=pk)
        context = {
            'food': food
        }
        return render(request, 'customer_operations/remove_like.html', context)

    def post(self, request, pk):
        food = Food.objects.get(id=pk)
        customer = Customer.objects.get(pk=request.user.customuser.customer.pk)
        food.likes.remove(customer)
        return redirect('liked_foods')


class RemoveOrderView(LoginRequiredMixin, View):
    def get(self, request, pk):
        food = Food.objects.get(id=pk)
        context = {
            'food': food
        }
        return render(request, 'customer_operations/remove_order.html', context)

    def post(self, request, pk):
        food = Food.objects.get(id=pk)
        customer = Customer.objects.get(pk=request.user.customuser.customer.pk)
        food.orders.remove(customer)
        return redirect('customer_show_orders')


class MakeCommentView(LoginRequiredMixin, View):
    def get(self, request, pk):
        food = Food.objects.get(id=pk)
        form = MakeCommentForm()
        context = {
            'food': food,
            'form': form
        }
        return render(request, 'customer_operations/make_comment.html', context)

    def post(self, request, pk):
        form = MakeCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            food = Food.objects.get(id=pk)
            customer = request.user.customuser.customer
            comment.customer = customer
            comment.food = food
            comment.save()
            return redirect('liked_foods')
        else:
            return redirect('/')


class ShowCustomerOwnCommentsView(LoginRequiredMixin, View):
    def get(self, request):
        customer = request.user.customuser.customer
        customer_comments = Comment.objects.filter(customer=customer)
        context = {
            'customer_comments': customer_comments,
        }
        print(context)
        return render(request, 'customer_operations/liked_foods.html', context)


class RemoveCommentView(LoginRequiredMixin, View):
    def get(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        context = {
            'comment': comment
        }
        return render(request, 'customer_operations/remove_comment.html', context)

    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return redirect('liked_foods')


class MakeOrderView(LoginRequiredMixin, View):
    def get(self, request, pk):
        food = Food.objects.get(id=pk)
        form = MakeOrderForm()
        context = {
            'food': food,
            'form': form
        }
        return render(request, 'customer_operations/make_order.html', context)

    def post(self, request, pk):
        form = MakeOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            food = Food.objects.get(id=pk)
            customer = request.user.customuser.customer
            order.customer = customer
            order.food = food
            order.status = 'Pending'
            order_count = food.order_count
            order_count = order_count + 1
            food.order_count = order_count
            restaurant_order_count = food.restaurant.ordered_food_count
            restaurant_order_count = restaurant_order_count + 1
            food.restaurant.ordered_food_count = restaurant_order_count
            food.restaurant.save()
            food.save()
            order.save()
            return redirect('customer_own_orders')
        else:
            return redirect('/')


class ShowCustomerOwnOrdersView(LoginRequiredMixin, View):
    def get(self, request):
        customer = request.user.customuser.customer
        orders = Order.objects.filter(customer=customer)
        context = {
            'customer': customer,
            'orders': orders,
        }
        print(context)
        return render(request, 'customer_operations/customer_own_orders.html', context)


class RemoveOrderCustomerView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        context = {
            'order': order
        }
        return render(request, 'customer_operations/remove_order_customer.html', context)

    def post(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        order_count = order.food.order_count
        order_count = order_count - 1
        order.food.order_count = order_count
        restaurant_order_count = order.food.restaurant.ordered_food_count
        restaurant_order_count = restaurant_order_count - 1
        order.food.restaurant.ordered_food_count = restaurant_order_count
        order.food.restaurant.save()
        order.food.save()
        return redirect('customer_own_orders')


class OtherCustomersProfileView(LoginRequiredMixin, View):
    def get(self, request, pk):
        context = {}
        return render(request, 'customer_operations/other_customers_profile.html', context)


class CheapestFoodsView(LoginRequiredMixin, View):
    def get(self, request):
        foods = Food.objects.all()
        cheapest_foods = foods.order_by('price')[:5]
        print(cheapest_foods)
        context = {
            'cheapest_foods': cheapest_foods
        }
        return render(request, 'customer_operations/cheapest_foods.html', context)


class PopularRestaurantsView(LoginRequiredMixin, View):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        most_ordered_restaurants = list(restaurants.order_by('-ordered_food_count')[:5])
        most_ordered_foods = {}
        for restaurant in most_ordered_restaurants:
            foods = Food.objects.filter(restaurant=restaurant)
            most_popular_food = foods.order_by('-order_count').first()
            most_ordered_foods[restaurant] = most_popular_food
        print(most_ordered_foods)
        context = {
            'most_ordered_restaurants': most_ordered_restaurants,
            'most_ordered_foods': most_ordered_foods
        }
        print(most_ordered_restaurants)
        return render(request, 'customer_operations/popular_restaurants.html', context)


class PopularFoodsView(LoginRequiredMixin, View):
    def get(self, request):
        foods = Food.objects.all()
        most_ordered_foods = foods.order_by('-order_count')[:5]
        context = {
            'most_ordered_foods': most_ordered_foods
        }
        return render(request, 'customer_operations/popular_foods.html', context)


class CheapestRestaurantsView(LoginRequiredMixin, View):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        foods = {}
        cheapest_foods = {}
        for restaurant in restaurants:
            calculate_avg_prices(restaurant)
            foods[restaurant] = Food.objects.filter(restaurant=restaurant)
            # cheapest_foods[restaurant] = foods[restaurant].order_by('price').first()
        print(cheapest_foods)
        ordered_avg_prices_restaurants = restaurants.order_by('avg_int_food_price')[:5]
        for restaurant in ordered_avg_prices_restaurants:
            cheapest_foods[restaurant] = foods[restaurant].order_by('price').first()
        context = {
            'restaurants': ordered_avg_prices_restaurants,
            'cheapest_foods': cheapest_foods
        }
        return render(request, 'customer_operations/cheapest_restaurants.html', context)


def calculate_avg_prices(restaurant):
    foods = Food.objects.filter(restaurant=restaurant)
    avg_price = foods.aggregate(Avg('price'))
    avg_int_price = int(avg_price['price__avg'])
    restaurant.avg_int_food_price = avg_int_price
    restaurant.save()


class MostLikedFoodsView(View):
    def get(self,request):
        foods = Food.objects.all()
        most_liked_foods = foods.order_by('-like_count')[:5]
        context = {
            'most_liked_foods': most_liked_foods
        }
        return render(request, 'customer_operations/most_liked_foods.html', context)


class RecommendedFood(LoginRequiredMixin, View):
    def get(self, request, pk):
        i = 0
        while i < customers_array.size:
            if customers_array[i] == pk:
                customer_cluster = kmeans.predict([category_count_customers[i]])
            i = i + 1
        j = 0
        while j < customers_array.size:
            if kmeans.predict([category_count_customers[j]]) == customer_cluster[0]:
                print('girdi')
                print(kmeans.predict([category_count_customers[j]])[0])
                print(j)
                print(category_count_customers[j])
                customer = Customer.objects.get(pk = customers_array[j])
                liked_foods = Food.objects.filter(likes__user=customer)
                random_num = random.randint(0, 8)
                recommended_food = liked_foods[random_num]
                print(recommended_food)
                print(random_num)
                print(customer.pk)
                j = customers_array.size + 1
            j = j+1
        context = {
            'recommended_food': recommended_food
        }
        return render(request, 'customer_operations/recommended_food.html', context)









