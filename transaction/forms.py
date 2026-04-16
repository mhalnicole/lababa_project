from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'order',
            'rider',
            'payment',
            'pickup_schedule',
            'delivery_schedule',
            'status',
            'payment_status'
        ]