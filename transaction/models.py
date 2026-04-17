from django.db import models
from order.models import Order

class Rider(models.Model):
    rider_id = models.CharField(max_length=20, primary_key=True)
    rider_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.rider_name


class Payment(models.Model):
    payment_id = models.CharField(max_length=20, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.payment_id


class PickupSchedule(models.Model):
    pickup_id = models.CharField(max_length=20, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.pickup_id


class DeliverySchedule(models.Model):
    delivery_id = models.CharField(max_length=20, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.delivery_id