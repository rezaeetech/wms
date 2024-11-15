from django.db import models


class Supplier(models.Model):
    name = models.CharField(
        max_length=150,
    )
    contact_number = models.CharField(
        verbose_name="Contact Number",
        max_length=20,
    )
    email = models.EmailField(
        verbose_name="Contact Email",
        blank=True,
        null=True,
        max_length=254,
    )
    address = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.name
