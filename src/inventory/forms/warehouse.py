from django import forms
from django.utils.translation import gettext_lazy as _

from inventory.models import Warehouse


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ["name", "location", "capacity"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": _("Enter Warehouse name"),
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": _("Enter Location"),
                }
            ),
            "capacity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": _("Enter Capacity"),
                }
            ),
        }
