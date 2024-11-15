from django.db import models
from django.utils.translation import gettext_lazy as _


class Warehouse(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=150,
    )
    location = models.CharField(
        verbose_name=_("Location"),
        max_length=255,
    )
    capacity = models.IntegerField(
        verbose_name=_("Capacity"),
    )

    def __str__(self):
        return self.name
