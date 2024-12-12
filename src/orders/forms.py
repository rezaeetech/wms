from django import forms
from django.forms import modelformset_factory
from django.utils.translation import gettext_lazy as _

from orders.models import (
    Order,
    OrderItems,
    Customer,
    InventoryTransaction,
)

from inventory.models import (
    Warehouse,
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


class InventoryTransactionForm(forms.ModelForm):
    class Meta:
        model = InventoryTransaction
        fields = ["transaction_type", "order", "warehouse"]
        widgets = {
            "transaction_type": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "order": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "warehouse": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }
        labels = {
            "transaction_type": _("Transaction Type"),
            "order": _("Order"),
            "warehouse": _("Warehouse"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional customization:
        #   Limit available orders to those that are active or relevant
        self.fields["order"].queryset = Order.objects.filter(
            status="approved"
        )  # Example filter
        self.fields["warehouse"].queryset = (
            Warehouse.objects.all()
        )  # Include all warehouses
