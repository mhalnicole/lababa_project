from django.contrib import admin
from .models import Supplier, Inventory, Expense, Employee

admin.site.register(Supplier)
admin.site.register(Inventory)
admin.site.register(Expense)
admin.site.register(Employee)
