from django.contrib import admin
from .models import LaundryShop, Service, LaundryType

admin.site.register(LaundryShop)
admin.site.register(Service)
admin.site.register(LaundryType)