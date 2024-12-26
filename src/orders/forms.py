from django import forms
from django.forms import modelformset_factory
from django.utils.translation import gettext_lazy as _

from orders.models import (
    Order,
    OrderItems,
    Customer,
)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer", "order_type"]

        widgets = {
            "customer": forms.Select(
                attrs={
                    "id": "customer",
                    "class": "form-control",
                    "width": "100px",
                }
            ),
            "order_type": forms.Select(
                attrs={
                    "id": "order_type",
                    "class": "form-control",
                }
            ),
        }


OrderItemFormSet = modelformset_factory(
    OrderItems,
    fields=("product", "quantity", "price"),
    widgets={
        "product": forms.Select(
            attrs={
                "id": "product",
                "class": "form-control",
            }
        ),
        "quantity": forms.NumberInput(
            attrs={
                "id": "quantity",
                "class": "form-control",
            }
        ),
        "price": forms.NumberInput(
            attrs={
                "id": "price",
                "class": "form-control",
                "readonly": "True",
            }
        ),
    },
    extra=1,  # Allow at least one blank form
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
