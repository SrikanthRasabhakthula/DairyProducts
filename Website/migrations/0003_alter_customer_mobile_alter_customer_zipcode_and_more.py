# Generated by Django 5.1 on 2024-09-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Website", "0002_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="mobile",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="customer",
            name="zipcode",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("CR", "Curd"),
                    ("ML", "Milk"),
                    ("LS", "Lassi"),
                    ("MS", "Milkshake"),
                    ("PN", "Paneer"),
                    ("GH", "Ghee"),
                    ("CZ", "Cheese"),
                    ("IC", "Ice-creams"),
                ],
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="composition",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="product",
            name="prodapp",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_image",
            field=models.ImageField(upload_to="product/images/"),
        ),
    ]
