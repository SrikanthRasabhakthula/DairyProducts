# Generated by Django 5.1 on 2024-09-27 10:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Website", "0004_cart"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                ("amount", models.FloatField()),
                (
                    "razorpay_order_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "razorpay_payment_status",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "razorpay_payment_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("paid", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderPlaced",
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
                ("quantity", models.PositiveBigIntegerField(default=1)),
                ("ordered_date", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Accepted", "Accepted"),
                            ("Packed", "Packed"),
                            ("On The Way", "On The Way"),
                            ("Delivered", "Delivered"),
                            ("Cancel", "Cancel"),
                            ("Pending", "Pending"),
                        ],
                        default="pending",
                        max_length=50,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Website.customer",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Website.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "payment",
                    models.ForeignKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Website.payment",
                    ),
                ),
            ],
        ),
    ]
