from django.db import models

# Create your models here.
class LaundryShop(models.Model):
    shop_id = models.CharField(max_length=20, primary_key=True)
    shop_name = models.CharField(max_length=100)

    def __str__(self):
        return self.shop_name


class Service(models.Model):
    service_id = models.CharField(max_length=20, primary_key=True)
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name


class LaundryType(models.Model):
    type_id = models.CharField(max_length=20, primary_key=True)
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name