from django.db import models
import uuid

class Order(models.Model):
    SERVICE_CHOICES = [
        ('Wash Only', 'Wash Only'),
        ('Wash & Dry', 'Wash & Dry'),
        ('Wash, Dry & Fold', 'Wash, Dry & Fold'),
        ('Dry Cleaning', 'Dry Cleaning'),
    ]

    LAUNDRY_CHOICES = [
        ('Regular Clothes', 'Regular Clothes'),
        ('Bedsheets', 'Bedsheets'),
        ('Blankets', 'Blankets'),
        ('Curtains', 'Curtains'),
        ('Delicates', 'Delicates'),
    ]

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

    order_id = models.CharField(max_length=20, unique=True, editable=False)
    customer_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    laundry_type = models.CharField(max_length=50, choices=LAUNDRY_CHOICES)
    weight_in_kilos = models.DecimalField(max_digits=5, decimal_places=2)
    promo_code = models.CharField(max_length=20, blank=True, null=True)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()
    delivery_address = models.TextField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    order_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    LAUNDRY_SHOP_CHOICES = [
        ('Clean Wash Laundry', 'Clean Wash Laundry'),
        ('Fresh Fold Laundry', 'Fresh Fold Laundry'),
        ('LABABA Laundry Shop', 'LABABA Laundry Shop'),
    ]

    laundry_shop = models.CharField(
        max_length=100,
        choices=LAUNDRY_SHOP_CHOICES
    )



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
        return f"{self.order_id} - {self.customer_name}"
