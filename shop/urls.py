from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.ShopIndex.as_view(), name='index'),
    path('addNewShop', views.AddShop.as_view(), name='addshop'),
    path('editShop/<str:shop_id>', views.EditShop.as_view(), name='editshop'),
    path('deleteShop/<str:shop_id>', views.DeleteShop.as_view(), name='deleteshop'),
]