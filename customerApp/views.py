from django.shortcuts import render

# Create your views here.
def customerMainPage(request):
    return render(request, 'customerMainPage.html')

