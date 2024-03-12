from django import forms
from .models import Customer, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']
        # Các trường khác cho biểu mẫu khách hàng

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'products']
        # Các trường khác cho biểu mẫu đơn hàng