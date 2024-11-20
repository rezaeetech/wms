from django import forms
from django.utils.translation import gettext_lazy as _

from inventory.models import Inventory


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ["product", "warehouse", "quantity"]
        widgets = {
            "product": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "warehouse": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": _("Enter Quantity"),
                }
            ),
        }
