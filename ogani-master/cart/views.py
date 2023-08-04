from django.shortcuts import render

# Create your views here.

def Shoping(request):
    return render(request, 'shoping-cart.html')