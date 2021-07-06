from django.shortcuts import render,redirect
from django.views import View
from .models import Comment, Food
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import get_user_type


class SearchRestaurant(LoginRequiredMixin, View):
    def get(self,request):
        context = {}
        return render(request, 'common/search_restaurant.html', context)


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
    #restaurant
    if(get_user_type(uid) == 1):
        return redirect('restaurant_main_page')
    else:
        return redirect('customer_main_page')


def show_orders(request):
    uid = request.user.id
    #restaurant
    if(get_user_type(uid) == 1):
        return redirect('restaurant_show_orders')
    else:
        return redirect('customer_own_orders')







