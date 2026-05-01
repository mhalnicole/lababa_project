from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addNewTransaction/', views.add_transaction),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('edit-profile/', views.edit_profile),
]