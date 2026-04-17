from django.db import models

# Create your models here.
from django.db import models

class LaundryShop(models.Model):
    shop_id = models.CharField(max_length=20, primary_key=True)
    shop_name = models.CharField(max_length=100)
    shop_address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    shop_manager = models.CharField(max_length=100)

    def __str__(self):
        return self.shop_name


class LaundryType(models.Model):
    type_id = models.CharField(max_length=20, primary_key=True)
    type_name = models.CharField(max_length=100)
    washing_instructions = models.CharField(max_length=255)

    def __str__(self):
        return self.type_name


class Service(models.Model):
    service_id = models.CharField(max_length=20, primary_key=True)
    shop = models.ForeignKey(LaundryShop, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100, unique=True)
    price_per_kilo = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_time = models.CharField(max_length=100)
    service_category = models.CharField(max_length=100)

    def __str__(self):
        return self.service_name