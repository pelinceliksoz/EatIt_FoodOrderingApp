from django.shortcuts import render

# Create your views here.
def customerMainPage(request):
    context = {}
    return render(request, 'customerApp/customerMainPage.html', context)



