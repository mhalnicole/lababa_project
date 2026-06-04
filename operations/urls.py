from django.urls import path
from . import views

urlpatterns = [
    path('addNewEmployee', views.addNewEmployee, name='addNewEmployee'),
    path('viewEmployees', views.viewEmployees, name='viewEmployees'),
    path('editEmployee/<str:employee_id>', views.editEmployee, name='editEmployee'),
    path('deleteEmployee/<str:employee_id>', views.deleteEmployee, name='deleteEmployee'),
]
