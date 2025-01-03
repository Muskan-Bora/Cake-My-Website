# Generated by Django 5.0 on 2024-04-30 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0029_allcategories_alter_anniversary_anniversary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anniversary',
            name='anniversary',
            field=models.CharField(choices=[('25A', '25th Anniversary Cakes'), ('1AC', '1st Anniversary Cakes'), ('APC', 'Anniversary Photo Cakes'), ('50A', '50th Anniversary Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='birthday',
            field=models.CharField(choices=[('BPC', 'Birthday Photo Cakes'), ('SBC', 'Special Birthday Cakes'), ('BC', '1st Birthday Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.CharField(choices=[('GH', 'Gift Hampers'), ('PC', 'Photo Cakes'), ('Wed', 'Wedding Cakes'), ('GC', 'Gourmet Cakes'), ('TC', 'Tea Cakes & Cookies'), ('EC', 'Eggless Cakes'), ('HC', 'Heart-Shaped Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='design',
            name='designing',
            field=models.CharField(choices=[('BSC', 'Baby Shower Cakes'), ('CTC', 'Cricket Theme Cakes'), ('JTC', 'Jungle Theme Cakes'), ('ANC', 'Alphabet & Number Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='dessert_cake',
            name='dessert_cake',
            field=models.CharField(choices=[('JC', 'Jar Cakes'), ('PS', 'Pastries'), ('CC', 'Cup Cakes'), ('BN', 'Brownies')], max_length=3),
        ),
        migrations.AlterField(
            model_name='flavour',
            name='flavour',
            field=models.CharField(choices=[('SC', 'Strawberry Cakes'), ('PC', 'Pineapple Cakes'), ('RC', 'Red Velvet Cakes'), ('CC', 'Chocolate Cakes'), ('FC', 'Fruit Cakes'), ('BSC', 'Butterscotch Cakes'), ('BC', 'Blackforest Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='kids',
            name='kids',
            field=models.CharField(choices=[('CTC', 'Cartoon Cakes'), ('PC', 'Princess Cakes'), ('SHC', 'SuperHero Cakes'), ('CC', 'Car Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='trend',
            name='trending',
            field=models.CharField(choices=[('PMC', 'Pull Me Up Cakes'), ('BC', 'Bomb Cakes'), ('SCB', 'Suprise Cake Box'), ('PC', 'Pinata Cakes')], max_length=3),
        ),
    ]
