from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='customer_index'),
    path('addNewCustomer/', views.add_new_customer, name='add_new_customer'),
    path('addNewRating/', views.add_new_rating, name='add_new_rating'),
    path('home/', views.home, name='home'),
]