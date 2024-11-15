# Generated by Django 4.2.16 on 2024-11-15 20:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=50, unique=True, verbose_name='SKU'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='capacity',
            field=models.IntegerField(verbose_name='Capacity'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='location',
            field=models.CharField(max_length=255, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Name'),
        ),
    ]