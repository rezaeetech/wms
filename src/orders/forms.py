from django import forms
from django.utils.translation import gettext_lazy as _

from orders.models import (
    Customer,
)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "contact_number", "email", "address"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": _("Enter Customer name"),
                }
            ),
            "contact_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": _("Enter Contact Number"),
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": _("Enter Customer Email"),
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": _("Enter address"),
                }
            ),
        }
