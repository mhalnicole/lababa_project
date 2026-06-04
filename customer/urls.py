from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='customer_index'),

    path('home/', views.home, name='home'),
    path('lababa-home/', views.lababa_home, name='lababa_home'),

    path('addNewCustomer/', views.add_new_customer, name='add_new_customer'),

    path('manage-customers/', views.manage_customers, name='manage_customers'),

    path('edit-customer/<int:id>/', views.edit_customer, name='edit_customer'),

    path('delete-customer/<int:id>/', views.delete_customer, name='delete_customer'),

    path('ratings/', views.add_new_rating, name='view_customer_ratings'),
]