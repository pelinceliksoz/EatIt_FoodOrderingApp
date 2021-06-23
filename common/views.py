from django.shortcuts import render
from restaurant_operations.models import Restaurant


def searchRestaurant(request):

    context = {}
    return render(request, 'common/search_restaurant.html', context)


