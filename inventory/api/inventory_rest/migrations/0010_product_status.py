# Generated by Django 4.0.3 on 2022-06-09 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory_rest", "0009_alter_product_product_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.CharField(default="NOT_CARTED", max_length=100),
        ),
    ]
