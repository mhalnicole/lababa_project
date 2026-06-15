from django.db import models
import uuid

from customer.models import Customer
from shop.models import LaundryShop, Service, LaundryType

class Order(models.Model):




    PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('GCash', 'GCash'),
        ('Credit Card', 'Credit Card'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Rider Assigned', 'Rider Assigned'),
        ('Picked Up', 'Picked Up'),
        ('In Laundry Process', 'In Laundry Process'),
        ('Ready for Delivery', 'Ready for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        'customer.Customer',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    laundry_shop = models.ForeignKey(
        'shop.LaundryShop',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    service = models.ForeignKey(
        'shop.Service',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    laundry_type = models.ForeignKey(
        'shop.LaundryType',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    order_id = models.CharField(max_length=20, unique=True, editable=False)
    weight_in_kilos = models.DecimalField(max_digits=5, decimal_places=2)
    promo_code = models.CharField(max_length=20, blank=True, null=True)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    delivery_address = models.TextField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    order_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True, null= True)





    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = 'ORD-' + str(uuid.uuid4().hex[:8]).upper()
        
        # Calculate total amount
        # Base: 50 pesos per kilo
        base_price = float(self.weight_in_kilos) * 50
        
        # Promo logic
        if self.promo_code == 'WELCOME10':
            self.total_amount = base_price * 0.9
        else:
            self.total_amount = base_price
            
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_id} - {self.customer.full_name}"
