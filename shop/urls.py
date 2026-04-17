from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ShopIndex.as_view(), name='index'),
    path('addNewShop', views.AddShop.as_view(), name='addshop'),
]