from django.urls import path
from . import views

urlpatterns = [
	path('shoping/', views.Shoping, name='shoping'),
]