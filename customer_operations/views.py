from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from common.models import Food, Comment
from customer_operations.forms import MakeCommentForm
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


class RemoveOrder(View):

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



# TO ELIMINATE THE REPETITION OF THE REMOVE RELATIONS BUT I GAVE ERROR. I WILL TRY IT LATER.
# def remove_relation_get(relation_food, request, pk, get_url):
#
#     if request.method == 'GET':
#         food = relation_food
#         context = {
#             'food': food
#         }
#         return render(request, get_url, context)
#
#
# def remove_relation_post(request, pk, post_redirect, relation):
#
#     if request.method == 'POST':
#         customer = Customer.objects.get(pk=request.user.customuser.customer.pk)
#         relation.remove(customer)
#         return redirect(post_redirect)
#
#
# class RemoveOrder(View):
#
#     def get(self, request, pk):
#
#         relation_food = Food.objects.get(id=pk)
#         remove_relation_get(relation_food, request, pk, 'customer_operations/remove_order.html')
#
#     def post(self, request, pk):
#
#         relation_food = Food.objects.get(id=pk)
#         remove_relation_post(request, pk, 'customer_show_orders', relation_food.orders)


class MakeComment(View):

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

            return redirect('/')
        else:
            return redirect('/')


class ShowCustomerOwnComments(View):

    def get(self, request):

        customer = request.user.customuser.customer
        customer_comments = Comment.objects.filter(customer=customer)
        context = {
            'customer_comments': customer_comments,
        }
        print(context)
        return render(request, 'customer_operations/liked_foods.html', context)


class RemoveComment(View):

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



