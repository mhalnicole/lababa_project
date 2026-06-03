from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('addNewTransaction/', views.add_transaction, name='add_transaction'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]