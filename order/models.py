from django.db import models


class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.IntegerField()

    def __str__(self):
        return self.code


class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)

    shop_id = models.CharField(max_length=50)
    service_id = models.CharField(max_length=50)
    type_id = models.CharField(max_length=50)

    promo = models.ForeignKey(PromoCode, on_delete=models.SET_NULL, null=True, blank=True)

    weight_in_kilos = models.DecimalField(max_digits=5, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    order_status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return self.order_id


from django.db import models

# Create your models here.
