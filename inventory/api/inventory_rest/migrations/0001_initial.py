# Generated by Django 4.0.3 on 2022-06-07 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Size",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sizes",
                    models.CharField(
                        choices=[
                            ("1.0 fl oz", "1.0 fl oz"),
                            ("2.0 fl oz", "2.0 fl oz"),
                            ("4.0 fl oz", "4.0 fl oz"),
                            ("8.0 fl oz", "8.0 fl oz"),
                            ("16.0 fl oz", "16.0 fl oz"),
                            ("1.0 oz", "1.0 oz"),
                            ("2.0 oz", "2.0 oz"),
                            ("4.0 oz", "4.0 oz"),
                            ("8.0 oz", "8.0 oz"),
                            ("16.0 oz", "16.0 oz"),
                        ],
                        default="",
                        max_length=25,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("sku", models.CharField(max_length=12, unique=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "scent1",
                    models.CharField(
                        choices=[
                            ("", "-----------"),
                            ("Fresh", "Fresh"),
                            ("Amber", "Amber"),
                            ("Floral", "Floral"),
                            ("Woody", "Woody"),
                            ("Fruity", "Fruity"),
                            ("Gourmand", "Gourmand"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "scent2",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("", "-----------"),
                            ("Fresh", "Fresh"),
                            ("Amber", "Amber"),
                            ("Floral", "Floral"),
                            ("Woody", "Woody"),
                            ("Fruity", "Fruity"),
                            ("Gourmand", "Gourmand"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "scent3",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("", "-----------"),
                            ("Fresh", "Fresh"),
                            ("Amber", "Amber"),
                            ("Floral", "Floral"),
                            ("Woody", "Woody"),
                            ("Fruity", "Fruity"),
                            ("Gourmand", "Gourmand"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "scent4",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("", "-----------"),
                            ("Fresh", "Fresh"),
                            ("Amber", "Amber"),
                            ("Floral", "Floral"),
                            ("Woody", "Woody"),
                            ("Fruity", "Fruity"),
                            ("Gourmand", "Gourmand"),
                        ],
                        max_length=25,
                    ),
                ),
                ("quantity", models.PositiveSmallIntegerField()),
                ("ingredients", models.CharField(max_length=500)),
                ("limited_item", models.BooleanField()),
                ("image", models.URLField()),
                ("description", models.CharField(max_length=400)),
                ("usage", models.CharField(max_length=100)),
                ("storage", models.CharField(max_length=100)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="products",
                        to="inventory_rest.size",
                    ),
                ),
            ],
            options={
                "ordering": ("size", "name"),
            },
        ),
    ]
