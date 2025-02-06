# Generated by Django 4.2.17 on 2025-01-03 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_tax_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tax_data',
        ),
        migrations.AlterField(
            model_name='order',
            name='total_tax',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
