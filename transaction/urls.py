from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addNewTransaction/', views.add_transaction),
]