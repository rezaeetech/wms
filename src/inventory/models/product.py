from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
    )
    sku = models.CharField(
        verbose_name=_("SKU"),
        max_length=50,
        unique=True,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        verbose_name=_("Price"),
        max_digits=12,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    category = models.ForeignKey(
        to="inventory.category",
        verbose_name=_("Category"),
        on_delete=models.SET_NULL,
        null=True,
    )
    supplier = models.ForeignKey(
        to="inventory.supplier",
        verbose_name=_("Supplier"),
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f"{self.name} (SKU: {self.sku})"
