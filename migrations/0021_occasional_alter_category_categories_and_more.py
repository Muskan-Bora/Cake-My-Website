# Generated by Django 5.0 on 2024-04-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0020_trend_alter_category_categories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occasional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occasion_code', models.IntegerField(default=50)),
                ('occasion_name', models.CharField(max_length=100)),
                ('occasion_desc', models.CharField(default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.', max_length=500)),
                ('occasion_price', models.IntegerField()),
                ('occasion_image', models.ImageField(default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125', upload_to='occasion')),
                ('occasion', models.CharField(choices=[('TC', 'Teachers Day Cake'), ('MFC', 'Mothers & Fathers Day Cakes'), ('DC', 'Doctors Dya Cake')], max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.CharField(choices=[('HC', 'Heart-Shaped Cakes'), ('PC', 'Photo Cakes'), ('GH', 'Gift Hampers'), ('GC', 'Gourmet Cakes'), ('Wed', 'Wedding Cakes'), ('EC', 'Eggless Cakes'), ('TC', 'Tea Cakes & Cookies')], max_length=3),
        ),
        migrations.AlterField(
            model_name='flavour',
            name='flavour',
            field=models.CharField(choices=[('CC', 'Chocolate Cakes'), ('BC', 'Blackforest Cakes'), ('FC', 'Fruit Cakes'), ('SC', 'Strawberry Cakes'), ('RC', 'Red Velvet Cakes'), ('BSC', 'Butterscotch Cakes'), ('PC', 'Pineapple Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='kids',
            name='kids',
            field=models.CharField(choices=[('SHC', 'SuperHero Cakes'), ('CC', 'Car Cakes'), ('PC', 'Princess Cakes'), ('CTC', 'Cartoon Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='trend',
            name='trending',
            field=models.CharField(choices=[('SCB', 'Suprise Cake Box'), ('PMC', 'Pull Me Up Cakes'), ('PC', 'Pinata Cakes'), ('BC', 'Bomb Cakes')], max_length=3),
        ),
    ]