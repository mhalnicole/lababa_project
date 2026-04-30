from django.urls import path
from . import views

urlpatterns = [
    path('addNewEmployee', views.addNewEmployee, name='addNewEmployee'),
]
