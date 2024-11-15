from django.db import models


class Warehouse(models.Model):
    name = models.CharField(
        max_length=150,
    )
    location = models.CharField(
        max_length=255,
    )
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
