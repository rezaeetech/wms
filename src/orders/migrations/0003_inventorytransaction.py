# Generated by Django 4.2.16 on 2024-12-01 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0003_alter_inventory_options_and_more'),
        ('orders', '0002_alter_customer_id_alter_order_id_alter_orderitems_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('inbound', 'Inbound'), ('outbound', 'Outbound')], max_length=10, verbose_name='Transaction Type')),
                ('transaction_date', models.DateTimeField(auto_now_add=True, verbose_name='Transaction Date')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_transactions', to='orders.order', verbose_name='Order')),
                ('recorded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Recorded By')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.warehouse', verbose_name='Warehouse')),
            ],
            options={
                'verbose_name': 'Inventory Transaction',
                'verbose_name_plural': 'Inventory Transactions',
                'ordering': ['-transaction_date'],
            },
        ),
    ]
