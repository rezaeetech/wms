from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=255,
    )
    sku = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
        verbose_name="Created at",
        auto_now_add=True,
    )

    category = models.ForeignKey(
        to="inventory.category",
        verbose_name="Category",
        on_delete=models.SET_NULL,
        null=True,
    )
    supplier = models.ForeignKey(
        "inventory.supplier",
        verbose_name="Supplier",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f"{self.name} (SKU: {self.sku})"
