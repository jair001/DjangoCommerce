from django import forms

from orders.models import OrderModel


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = (
            "date_emi",
            "customer", "billing_address",
            "shipping_address",
            "payment_mode"
        )