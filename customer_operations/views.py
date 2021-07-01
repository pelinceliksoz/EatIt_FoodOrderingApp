from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from common.models import Food, Comment, Order
from customer_operations.forms import MakeCommentForm,MakeOrderForm
from restaurant_operations.models import Restaurant
from customer_operations.models import Customer
from django.urls import reverse
from django.http import HttpResponseRedirect


class CustomerMainPageView(View):
    def get(self, request):
        user_name = request.user.first_name
        all_restaurants = Restaurant.objects.all().order_by('restaurant_name')
        context = {
            'user_name': user_name,
            'all_restaurants': all_restaurants,
        }
        return render(request, 'customer_operations/customer_main_page.html', context)


class FoodDetailsView(View):
    def get(self, request, pk):
        food = Food.objects.get(pk=pk)
        stuff = get_object_or_404(Food, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        order_form = MakeOrderForm()
        comment_form = MakeCommentForm()
        context = {
            'food': food,
            'total_likes': total_likes,
            'order_form': order_form,
            'comment_form': comment_form
        }
        return render(request, 'customer_operations/food_details.html', context)


# class MakeCommentView(View):
#     def get(self, request, pk):
#         customer = Customer.objects.get(pk=pk)
#         food = Food.objects.get(pk=pk)
#         context = {
#             'customer': customer,
#             'food': food
#         }
#         return render(request, 'customer_operations/food_details.html', context)


class LikeView(View):
    def post(self, request, pk):
        food = get_object_or_404(Food, id=request.POST.get('food_pk'))
        food.likes.add(request.user.customuser.customer)
        return HttpResponseRedirect(reverse('food_details', args=[str(pk)]))


class LikedFoodsView(View):
    def get(self, request):
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


class RemoveLikeView(View):
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


class RemoveOrderView(View):
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


class MakeCommentView(View):
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
            return redirect('food_details', pk=food.pk)
        else:
            return redirect('/')


class ShowCustomerOwnCommentsView(View):
    def get(self, request):
        customer = request.user.customuser.customer
        customer_comments = Comment.objects.filter(customer=customer)
        context = {
            'customer_comments': customer_comments,
        }
        print(context)
        return render(request, 'customer_operations/liked_foods.html', context)


class RemoveCommentView(View):
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


class MakeOrderView(View):
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
            order.save()
            return redirect('food_details', pk=food.pk)
        else:
            return redirect('/')


class ShowCustomerOwnOrdersView(View):
    def get(self, request):
        customer = request.user.customuser.customer
        orders = Order.objects.filter(customer=customer)
        context = {
            'customer': customer,
            'orders': orders,
        }
        print(context)
        return render(request, 'customer_operations/customer_own_orders.html', context)


class RemoveOrderCustomerView(View):
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




