from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        verbose_name=_("Category Name"),
        max_length=150,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
