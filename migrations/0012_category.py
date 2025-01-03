# Generated by Django 5.0 on 2024-04-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_desserts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.IntegerField(default=20)),
                ('category_name', models.CharField(max_length=100)),
                ('category_desc', models.CharField(default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.', max_length=500)),
                ('category_price', models.IntegerField()),
                ('category_image', models.ImageField(default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125', upload_to='category')),
                ('categories', models.CharField(choices=[('HC', 'Heart-Shaped Cakes'), ('EC', 'Eggless Cakes'), ('PC', 'Photo Cakes'), ('WC', 'Wedding Cakes'), ('GC', 'Gourmet Cakes'), ('TC', 'Tea Cakes & Cookies'), ('GH', 'Gift Hampers')], max_length=3)),
            ],
        ),
    ]
