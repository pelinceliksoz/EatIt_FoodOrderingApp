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
from django.db.models import Avg

class CustomerMainPageView(LoginRequiredMixin, View):
    def get(self, request):
        user_name = request.user.first_name
        all_restaurants = Restaurant.objects.all().order_by('restaurant_name')
        context = {
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
        if stuff.likes.filter(user_id=request.user.id).exists():
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
        # like_count = food.likes.count()
        # food.rate = like_count
        # food.rate.save()

        if food.likes.filter(user_id=request.user.id).exists():
            food.likes.remove(request.user.customuser.customer)
            liked = False
        else:
            food.likes.add(request.user.customuser.customer)
            liked = True
        html = render_to_string(template_name='djangoP/like.html', context={'liked': liked})
        return JsonResponse({'liked': liked})


class LikedFoodsView(LoginRequiredMixin, View):
    def get(self, request):
        # restaurant
        if (get_user_type(request.user.id) == 1):
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

        # orders = Order.objects.all().values('food__restaurant').annotate(total=Count('food_restaurant').order_by('total'))
        # print(orders)
        # orders = Order.objects.all()
        # restaurants = Restaurant.objects.all()
        # for order in orders:
        #     for restaurant in restaurants:
        #         if order.food.restaurant == restaurant:
        #
        context = {

        }
        return render(request, 'customer_operations/popular_restaurants.html', context)


class PopularFoodsView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
        }
        return render(request, 'customer_operations/popular_foods.html', context)


class CheapestRestaurantsView(LoginRequiredMixin, View):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        for restaurant in restaurants:
            calculate_avg_prices(restaurant)
        ordered_avg_prices_restaurants = restaurants.order_by('avg_int_food_price')[:5]
        context = {
            'restaurants': ordered_avg_prices_restaurants
        }
        return render(request, 'customer_operations/cheapest_restaurants.html', context)


def calculate_avg_prices(restaurant):
    foods = Food.objects.filter(restaurant=restaurant)
    avg_price = foods.aggregate(Avg('price'))
    avg_int_price = int(avg_price['price__avg'])
    restaurant.avg_int_food_price = avg_int_price
    restaurant.save()









