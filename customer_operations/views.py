from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from common.models import Food
from restaurant_operations.models import Restaurant
from customer_operations.models import Customer
from django.urls import reverse
from django.http import HttpResponseRedirect


class CustomerMainPage(View):

    def get(self, request):

        user_name = request.user.first_name
        all_restaurants = Restaurant.objects.all().order_by('restaurant_name')

        context = {
            'user_name': user_name,
            'all_restaurants': all_restaurants,
        }
        return render(request, 'customer_operations/customer_main_page.html', context)


class FoodDetails(View):

    def get(self, request, pk):

        food = Food.objects.get(pk=pk)
        stuff = get_object_or_404(Food, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context = {
            'food': food,
            'total_likes': total_likes
        }
        return render(request, 'customer_operations/food_details.html', context)


class MakeComment(View):

    def get(self, request, pk):

        customer = Customer.objects.get(pk=pk)
        food = Food.objects.get(pk=pk)
        context = {
            'customer': customer,
            'food': food
        }
        return render(request, 'customer_operations/food_details.html', context)


class LikeView(View):

    def post(self, request, pk):
        food = get_object_or_404(Food, id=request.POST.get('food_pk'))
        food.likes.add(request.user.customuser.customer)
        return HttpResponseRedirect(reverse('food_details', args=[str(pk)]))


class LikedFoods(View):

    def get(self, request):

        customer_name = Customer.objects.get(pk=request.user.customuser.customer.pk)
        liked_foods = Food.objects.filter(likes=request.user.customuser.customer)

        # customer = Customer.objects.get(user=request.user.customuser.customer)
        # liked_foods = Food.likes.get(customer=customer)
        context = {
            'customer_name': customer_name,
            'liked_foods': liked_foods
        }
        return render(request, 'customer_operations/liked_foods.html', context)


class RemoveLike(View):

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


class ConfirmOrderCustomer(View):

    def get(self, request, pk):

        food = Food.objects.get(id=pk)
        context = {
            'food': food
        }
        return render(request, 'customer_operations/confirm_order_customer.html', context)

    def post(self, request, pk):

        food = Food.objects.get(id=pk)
        food.orders.add(request.user.customuser.customer)
        return redirect('/')


class CustomerShowOrders(View):

    def get(self, request):

        customer_name = Customer.objects.get(pk=request.user.customuser.customer.pk)
        ordered_foods = Food.objects.filter(orders=request.user.customuser.customer)

        context = {
            'customer_name': customer_name,
            'ordered_foods': ordered_foods
        }
        return render(request, 'customer_operations/customer_show_orders.html', context)


















