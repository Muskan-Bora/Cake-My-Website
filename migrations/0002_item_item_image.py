# Generated by Django 5.0 on 2023-12-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125', max_length=500),
        ),
    ]
