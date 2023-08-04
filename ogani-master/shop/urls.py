from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
	path('', views.Index, name='index'),
	path('blog/', views.Blog, name='blog'),
	path('blogDetails/', views.BlogDetails, name='blogDetails'),
	path('shopDetails/', views.ShopDetails, name='shopDetails'),
	path('shopGrid/', views.ShopGrid, name='shopGrid'),
]