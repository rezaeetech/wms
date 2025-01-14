# Generated by Django 4.2.16 on 2024-12-01 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_inventory_created_at_product_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'Inventory', 'verbose_name_plural': 'Inventories'},
        ),
        migrations.AlterUniqueTogether(
            name='inventory',
            unique_together={('product', 'warehouse')},
        ),
    ]
