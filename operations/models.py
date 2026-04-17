from django.db import models

# Create your models here.
class Supplier(models.Model):
    supplier_id = models.CharField(max_length=20, primary_key=True)
    supplier_name = models.CharField(max_length=100)

    def __str__(self):
        return self.supplier_name


class Inventory(models.Model):
    inventory_id = models.CharField(max_length=20, primary_key=True)
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item_name


class Expense(models.Model):
    expense_id = models.CharField(max_length=20, primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.expense_id


class Employee(models.Model):
    employee_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name