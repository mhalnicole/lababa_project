from django.db import models
from customer.models import Customer

class PromoCode(models.Model):
    promo_id = models.CharField(max_length=20, primary_key=True)
    code = models.CharField(max_length=50)
    discount = models.IntegerField()

    def __str__(self):
        return self.code


class Order(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_id