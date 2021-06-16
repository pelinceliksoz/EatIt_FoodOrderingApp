from django.shortcuts import render

# Create your views here.
def restaurantMainPage(request):
    return render(request, 'restaurantMainPage.html')