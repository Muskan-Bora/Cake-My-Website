# Generated by Django 5.0 on 2024-12-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0041_alter_anniversary_anniversary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anniversary',
            name='anniversary',
            field=models.CharField(choices=[('APC', 'Anniversary Photo Cakes'), ('1AC', '1st Anniversary Cakes'), ('25A', '25th Anniversary Cakes'), ('50A', '50th Anniversary Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='birthday',
            field=models.CharField(choices=[('BC', '1st Birthday Cakes'), ('SBC', 'Special Birthday Cakes'), ('BPC', 'Birthday Photo Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.CharField(choices=[('HC', 'Heart-Shaped Cakes'), ('TC', 'Tea Cakes & Cookies'), ('GH', 'Gift Hampers'), ('GC', 'Gourmet Cakes'), ('Wed', 'Wedding Cakes'), ('PC', 'Photo Cakes'), ('EC', 'Eggless Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='design',
            name='designing',
            field=models.CharField(choices=[('BSC', 'Baby Shower Cakes'), ('JTC', 'Jungle Theme Cakes'), ('ANC', 'Alphabet & Number Cakes'), ('CTC', 'Cricket Theme Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='dessert_cake',
            name='dessert_cake',
            field=models.CharField(choices=[('BN', 'Brownies'), ('CC', 'Cup Cakes'), ('PS', 'Pastries'), ('JC', 'Jar Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='flavour',
            name='flavour',
            field=models.CharField(choices=[('RC', 'Red Velvet Cakes'), ('BC', 'Blackforest Cakes'), ('PC', 'Pineapple Cakes'), ('SC', 'Strawberry Cakes'), ('FC', 'Fruit Cakes'), ('BSC', 'Butterscotch Cakes'), ('CC', 'Chocolate Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='kids',
            name='kids',
            field=models.CharField(choices=[('PC', 'Princess Cakes'), ('CC', 'Car Cakes'), ('CTC', 'Cartoon Cakes'), ('SHC', 'SuperHero Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='occasional',
            name='occasion',
            field=models.CharField(choices=[('TC', 'Teachers Day Cake'), ('MFC', 'Mothers & Fathers Day Cakes'), ('DC', 'Doctors Dya Cake')], max_length=3),
        ),
        migrations.AlterField(
            model_name='trend',
            name='trending',
            field=models.CharField(choices=[('BC', 'Bomb Cakes'), ('PC', 'Pinata Cakes'), ('SCB', 'Suprise Cake Box'), ('PMC', 'Pull Me Up Cakes')], max_length=3),
        ),
    ]
