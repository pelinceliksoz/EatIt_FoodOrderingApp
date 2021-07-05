from django.shortcuts import render
from django.views import View
from .models import Comment, Food
from django.contrib.auth.mixins import LoginRequiredMixin

from restaurant_operations.models import Restaurant


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



