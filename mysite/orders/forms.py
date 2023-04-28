from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'region', 'city', 'street_name', 'house_number',
                  'case_number', 'apartment_number', 'postal_code']
