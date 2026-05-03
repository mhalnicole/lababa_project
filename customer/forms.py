from django import forms
from .models import Customer, Rating


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'