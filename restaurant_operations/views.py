from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddFoodForm, ChangeOrderStatusForm
from .models import Restaurant
from common.models import Food, Order, Customer, Comment
from accounts.models import CustomUser
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import get_user_type


class RestaurantMainPageView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddFoodForm()
        user_id = request.user.id
        restaurant = Restaurant.objects.get(user__user_id=user_id)
        restaurant_foods = Food.objects.filter(restaurant=restaurant)

        context = {
            'form': form,
            'restaurant': restaurant,
            'foods': restaurant_foods
        }
        return render(request, 'restaurant_operations/restaurant_main_page.html', context)


class AddFoodView(LoginRequiredMixin, View):
    def get(self, request, restaurant_id):
        restaurant = Restaurant.objects.get(user_id=restaurant_id)
        form = AddFoodForm()
        context = {
            'form': form,
            'restaurant': restaurant,
        }
        return render(request, "restaurant_operations/add_food.html", context)

    def post(self, request, restaurant_id):
        form = AddFoodForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            food = form.save()
            restaurant = Restaurant.objects.get(user_id=restaurant_id)
            food.restaurant = restaurant
            food.save()

            context = {
                'restaurant': restaurant
            }
            return redirect('restaurant_main_page')
        else:
            print(form.errors)
            return


class RestaurantMenuView(LoginRequiredMixin, View):
    def get(self, request, pk):
        requested_restaurant = Restaurant.objects.get(user_id=pk)
        foods = Food.objects.filter(restaurant=requested_restaurant)
        context = {
            'restaurant': requested_restaurant,
            'foods': foods
        }
        return render(request, 'restaurant_operations/restaurant_menu.html', context)


class UpdateFoodView(LoginRequiredMixin, View):
    def get(self, request, pk):
        food = Food.objects.get(id=pk)
        form = AddFoodForm(instance=food)
        context = {
            'form': form,
            'food': food
        }
        return render(request, 'restaurant_operations/update_food.html', context)

    def post(self, request, pk):
        food = Food.objects.get(pk=pk)
        form = AddFoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('restaurant_main_page')
        context = {
            'food': food,
            'form': form
        }
        return render(request, 'restaurant_operations/update_food.html', context)


class DeleteFoodView(LoginRequiredMixin, View):
    def get(self, request, pk):
        food = Food.objects.get(id=pk)
        context = {
            'item': food
        }
        return render(request, 'restaurant_operations/delete_food.html', context)

    def post(self, request, pk):
        food = Food.objects.get(pk=pk)
        food.delete()
        return redirect('restaurant_main_page')


class RestaurantShowOrdersView(LoginRequiredMixin, View):
    def get(self, request):
        restaurant = request.user.customuser.restaurant
        orders = Order.objects.filter(food__restaurant=restaurant)
        form = ChangeOrderStatusForm(request.POST)
        context = {
            'restaurant': restaurant,
            'orders': orders,
            'form': form
        }
        return render(request, 'restaurant_operations/restaurant_show_orders.html', context)


class ChangeOrderStatusView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        form = ChangeOrderStatusForm(instance=order)
        context = {
            'form': form,
            'order': order
        }
        return render(request, 'restaurant_operations/change_order_status.html', context)

    def post(self, request, pk):
        order = Order.objects.get(pk=pk)
        form = ChangeOrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('restaurant_show_orders')
        context = {
            'order': order,
            'form': form
        }
        return render(request, 'restaurant_operations/restaurant_show_orders.html', context)


class RestaurantLikeComments(View):
    def get(self, request):
        context = {}
        return render(request, 'restaurant_operations/restaurant_likes_comments.html', context)


class RestaurantFoodDetails(View):
    def get(self, request, pk):
        food = Food.objects.get(pk=pk)
        context = {
            'food': food
        }
        return render(request, 'restaurant_operations/restaurant_food_details.html', context)


class RestaurantCustomerProfile(View):
    def get(self, request, pk):
        if(get_user_type(request.user.id) == 1):
            restaurant = request.user.customuser.restaurant
            user = User.objects.get(pk=pk)
            custom_user = CustomUser.objects.get(pk=pk)
            customer = Customer.objects.get(pk=pk)
            liked_foods = Food.objects.filter(likes=customer, restaurant__user=restaurant)
            customer_comments = Comment.objects.filter(customer=customer, food__restaurant__user=restaurant)
            orders = Order.objects.filter(customer=customer, food__restaurant__user=restaurant)

            context = {
                'user': user,
                'custom_user': custom_user,
                'customer': customer,
                'liked_foods': liked_foods,
                'restaurant': restaurant,
                'customer_comments': customer_comments,
                'orders': orders
            }
            return render(request, 'restaurant_operations/restaurant_customer_profile.html', context)
        else:
            user = User.objects.get(pk=pk)
            custom_user = CustomUser.objects.get(pk=pk)
            customer = Customer.objects.get(pk=pk)
            context = {
                'user': user,
                'custom_user': custom_user,
                'customer': customer,
            }
            return render(request, 'customer_operations/other_customers_profile.html', context)

