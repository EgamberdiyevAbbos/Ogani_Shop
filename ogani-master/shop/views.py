from django.shortcuts import render

# Create your views here.

def Blog(request):
    return render(request, 'app/blog.html')

def BlogDetails(request):
    return render(request, 'app/blog-details.html')
    
def Index(request):
    return render(request, 'app/index.html')
    
def ShopDetails(request):
    return render(request, 'app/shop-details.html')
    
def ShopGrid(request):
    return render(request, 'app/shop-grid.html')