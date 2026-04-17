from django import forms
from .models import LaundryShop

class ShopForm(forms.ModelForm):
    class Meta:
        model = LaundryShop
        fields = '__all__'