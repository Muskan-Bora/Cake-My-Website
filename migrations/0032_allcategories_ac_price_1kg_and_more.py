# Generated by Django 5.0 on 2024-12-14 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0031_alter_anniversary_anniversary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcategories',
            name='ac_price_1kg',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='allcategories',
            name='ac_price_250gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='allcategories',
            name='ac_price_500gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AlterField(
            model_name='anniversary',
            name='anniversary',
            field=models.CharField(choices=[('50A', '50th Anniversary Cakes'), ('25A', '25th Anniversary Cakes'), ('1AC', '1st Anniversary Cakes'), ('APC', 'Anniversary Photo Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='birthday',
            field=models.CharField(choices=[('BPC', 'Birthday Photo Cakes'), ('BC', '1st Birthday Cakes'), ('SBC', 'Special Birthday Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.CharField(choices=[('HC', 'Heart-Shaped Cakes'), ('EC', 'Eggless Cakes'), ('GC', 'Gourmet Cakes'), ('Wed', 'Wedding Cakes'), ('GH', 'Gift Hampers'), ('PC', 'Photo Cakes'), ('TC', 'Tea Cakes & Cookies')], max_length=3),
        ),
        migrations.AlterField(
            model_name='design',
            name='designing',
            field=models.CharField(choices=[('BSC', 'Baby Shower Cakes'), ('ANC', 'Alphabet & Number Cakes'), ('CTC', 'Cricket Theme Cakes'), ('JTC', 'Jungle Theme Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='dessert_cake',
            name='dessert_cake',
            field=models.CharField(choices=[('PS', 'Pastries'), ('JC', 'Jar Cakes'), ('BN', 'Brownies'), ('CC', 'Cup Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='flavour',
            name='flavour',
            field=models.CharField(choices=[('SC', 'Strawberry Cakes'), ('RC', 'Red Velvet Cakes'), ('BC', 'Blackforest Cakes'), ('CC', 'Chocolate Cakes'), ('FC', 'Fruit Cakes'), ('PC', 'Pineapple Cakes'), ('BSC', 'Butterscotch Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='kids',
            name='kids',
            field=models.CharField(choices=[('CC', 'Car Cakes'), ('SHC', 'SuperHero Cakes'), ('CTC', 'Cartoon Cakes'), ('PC', 'Princess Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='occasional',
            name='occasion',
            field=models.CharField(choices=[('MFC', 'Mothers & Fathers Day Cakes'), ('TC', 'Teachers Day Cake'), ('DC', 'Doctors Dya Cake')], max_length=3),
        ),
        migrations.AlterField(
            model_name='trend',
            name='trending',
            field=models.CharField(choices=[('BC', 'Bomb Cakes'), ('PMC', 'Pull Me Up Cakes'), ('SCB', 'Suprise Cake Box'), ('PC', 'Pinata Cakes')], max_length=3),
        ),
    ]