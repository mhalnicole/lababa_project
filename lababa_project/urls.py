from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('customer.urls')),
    path('admin/', admin.site.urls),
    path('customer/', include('customer.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]