from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(max_length=20, primary_key=True)
    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Rating(models.Model):
    rating_id = models.CharField(max_length=20, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    score = models.IntegerField()
    feedback = models.TextField()

    def __str__(self):
        return self.rating_id