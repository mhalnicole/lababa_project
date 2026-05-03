from django.db import models


class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class Rating(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    score = models.IntegerField()
    feedback = models.TextField()

    def __str__(self):
        return f"{self.customer.full_name} - {self.score}"