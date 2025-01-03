# Generated by Django 5.0 on 2024-12-14 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0032_allcategories_ac_price_1kg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anniversary',
            name='anniversary',
            field=models.CharField(choices=[('APC', 'Anniversary Photo Cakes'), ('25A', '25th Anniversary Cakes'), ('1AC', '1st Anniversary Cakes'), ('50A', '50th Anniversary Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='birthday',
            field=models.CharField(choices=[('SBC', 'Special Birthday Cakes'), ('BPC', 'Birthday Photo Cakes'), ('BC', '1st Birthday Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.CharField(choices=[('GH', 'Gift Hampers'), ('GC', 'Gourmet Cakes'), ('TC', 'Tea Cakes & Cookies'), ('HC', 'Heart-Shaped Cakes'), ('Wed', 'Wedding Cakes'), ('EC', 'Eggless Cakes'), ('PC', 'Photo Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='design',
            name='designing',
            field=models.CharField(choices=[('JTC', 'Jungle Theme Cakes'), ('BSC', 'Baby Shower Cakes'), ('ANC', 'Alphabet & Number Cakes'), ('CTC', 'Cricket Theme Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='dessert_cake',
            name='dessert_cake',
            field=models.CharField(choices=[('CC', 'Cup Cakes'), ('PS', 'Pastries'), ('BN', 'Brownies'), ('JC', 'Jar Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='flavour',
            name='flavour',
            field=models.CharField(choices=[('BC', 'Blackforest Cakes'), ('SC', 'Strawberry Cakes'), ('BSC', 'Butterscotch Cakes'), ('RC', 'Red Velvet Cakes'), ('CC', 'Chocolate Cakes'), ('FC', 'Fruit Cakes'), ('PC', 'Pineapple Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='kids',
            name='kids',
            field=models.CharField(choices=[('PC', 'Princess Cakes'), ('CTC', 'Cartoon Cakes'), ('SHC', 'SuperHero Cakes'), ('CC', 'Car Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='trend',
            name='trending',
            field=models.CharField(choices=[('PC', 'Pinata Cakes'), ('PMC', 'Pull Me Up Cakes'), ('SCB', 'Suprise Cake Box'), ('BC', 'Bomb Cakes')], max_length=3),
        ),
    ]
