# Generated by Django 5.0 on 2024-04-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0022_design_alter_category_categories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday_code', models.IntegerField(default=70)),
                ('birthday_name', models.CharField(max_length=100)),
                ('birthday_desc', models.CharField(default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.', max_length=500)),
                ('birthday_price', models.IntegerField()),
                ('birthday_image', models.ImageField(default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125', upload_to='birthday')),
                ('birthday', models.CharField(choices=[('BC', '1st Birthday Cakes'), ('BPC', 'Birthday Photo Cakes'), ('SBC', 'Special Birthday Cakes')], max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.CharField(choices=[('GC', 'Gourmet Cakes'), ('TC', 'Tea Cakes & Cookies'), ('PC', 'Photo Cakes'), ('Wed', 'Wedding Cakes'), ('HC', 'Heart-Shaped Cakes'), ('GH', 'Gift Hampers'), ('EC', 'Eggless Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='design',
            name='designing',
            field=models.CharField(choices=[('ANC', 'Alphabet & Number Cakes'), ('CTC', 'Cricket Theme Cakes'), ('JTC', 'Jungle Theme Cakes'), ('BSC', 'Baby Shower Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='flavour',
            name='flavour',
            field=models.CharField(choices=[('BSC', 'Butterscotch Cakes'), ('SC', 'Strawberry Cakes'), ('CC', 'Chocolate Cakes'), ('FC', 'Fruit Cakes'), ('PC', 'Pineapple Cakes'), ('BC', 'Blackforest Cakes'), ('RC', 'Red Velvet Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='kids',
            name='kids',
            field=models.CharField(choices=[('SHC', 'SuperHero Cakes'), ('PC', 'Princess Cakes'), ('CTC', 'Cartoon Cakes'), ('CC', 'Car Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='occasional',
            name='occasion',
            field=models.CharField(choices=[('MFC', 'Mothers & Fathers Day Cakes'), ('DC', 'Doctors Dya Cake'), ('TC', 'Teachers Day Cake')], max_length=3),
        ),
        migrations.AlterField(
            model_name='trend',
            name='trending',
            field=models.CharField(choices=[('SCB', 'Suprise Cake Box'), ('PC', 'Pinata Cakes'), ('BC', 'Bomb Cakes'), ('PMC', 'Pull Me Up Cakes')], max_length=3),
        ),
    ]
