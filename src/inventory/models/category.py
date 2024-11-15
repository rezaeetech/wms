from uuid import uuid4

from django.db import models


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
    )
    name = models.CharField(
        max_length=150,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
