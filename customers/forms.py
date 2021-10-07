from django import forms

# forms.Form permite crear a mano los campos
# forms.ModelForm permite crear los campos de acuerdo al modelo
from django.core.exceptions import ValidationError

from customers.models import CustomerModel


class BasicCustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ("full_name", "dni")

    def clean_dni(self):
        dni = self.cleaned_data.get("dni")
        if len(dni) < 10:
            raise ValidationError("Error, número menor a 10 dígitos")
        return dni