from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.index, name='index'),
    path('create/', views.create_order, name='create_order'),
    path('success/', views.success, name='success'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout_view, name='logout'),
]