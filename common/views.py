from django.shortcuts import render
from django.views import View
from .models import Comment, Food

from restaurant_operations.models import Restaurant


def searchRestaurant(request):

    context = {}
    return render(request, 'common/search_restaurant.html', context)


class SeeComments(View):

    def get(self, request, pk):

        food = Food.objects.get(pk=pk)
        comments = Comment.objects.filter(food=food)
        context = {
            'comments': comments
        }
        return render(request, 'common/see_comments.html', context)



