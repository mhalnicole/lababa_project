from django import forms
from django.utils import timezone
from datetime import time
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'pickup_date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'pickup_time': forms.TimeInput(attrs={
                'type': 'time'
            }),
            'order_status': forms.HiddenInput(),
        }

    def clean_pickup_date(self):
        pickup_date = self.cleaned_data.get('pickup_date')

        if pickup_date < timezone.localdate():
            raise forms.ValidationError("Pickup date cannot be before today's date.")

        return pickup_date

    def clean_pickup_time(self):
        pickup_time = self.cleaned_data.get('pickup_time')

        opening_time = time(8, 0)
        closing_time = time(17, 0)

        if pickup_time < opening_time or pickup_time > closing_time:
            raise forms.ValidationError("Pickup time must be between 8:00 AM and 5:00 PM.")

        return pickup_time