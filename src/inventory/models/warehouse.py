from uuid import uuid4

from django.db import models


class Warehouse(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
    )
    name = models.CharField(
        max_length=150,
    )
    location = models.CharField(
        max_length=255,
    )
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
