# Generated by Django 4.1.3 on 2023-06-29 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('order', '0004_rename_id_order_orderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
