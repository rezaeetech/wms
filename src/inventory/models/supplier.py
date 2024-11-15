from django.db import models
from django.utils.translation import gettext_lazy as _


class Supplier(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=150,
    )
    contact_number = models.CharField(
        verbose_name=_("Contact Number"),
        max_length=20,
    )
    email = models.EmailField(
        verbose_name=_("Contact Email"),
        blank=True,
        null=True,
        max_length=254,
    )
    address = models.CharField(
        verbose_name=_("Address"),
        max_length=255,
    )

    def __str__(self):
        return self.name
