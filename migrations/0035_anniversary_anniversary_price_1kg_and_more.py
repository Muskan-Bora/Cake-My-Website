# Generated by Django 5.0 on 2024-12-14 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0034_alter_anniversary_anniversary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anniversary',
            name='anniversary_price_1kg',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='anniversary',
            name='anniversary_price_250gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='anniversary',
            name='anniversary_price_500gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='birthday',
            name='birthday_price_1kg',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='birthday',
            name='birthday_price_250gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='birthday',
            name='birthday_price_500gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='category',
            name='categories_price_1kg',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='category',
            name='categories_price_250gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='category',
            name='categories_price_500gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='design',
            name='designing_price_1kg',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='design',
            name='designing_price_250gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='design',
            name='designing_price_500gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='dessert_cake',
            name='dessert_price_1kg',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='dessert_cake',
            name='dessert_price_250gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='dessert_cake',
            name='dessert_price_500gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='flavour',
            name='flavour_price_1kg',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='flavour',
            name='flavour_price_250gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='flavour',
            name='flavour_price_500gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='item',
            name='item_price_1kg',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='item',
            name='item_price_250gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='item',
            name='item_price_500gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='kids',
            name='kids_price_1kg',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='kids',
            name='kids_price_250gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='kids',
            name='kids_price_500gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='occasional',
            name='occasion_price_1kg',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='occasional',
            name='occasion_price_250gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='occasional',
            name='occasion_price_500gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='trend',
            name='trending_price_1kg',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='trend',
            name='trending_price_250gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AddField(
            model_name='trend',
            name='trending_price_500gm',
            field=models.DecimalField(decimal_places=2, default='10.5', max_digits=6),
        ),
        migrations.AlterField(
            model_name='anniversary',
            name='anniversary',
            field=models.CharField(choices=[('1AC', '1st Anniversary Cakes'), ('50A', '50th Anniversary Cakes'), ('APC', 'Anniversary Photo Cakes'), ('25A', '25th Anniversary Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='birthday',
            field=models.CharField(choices=[('BPC', 'Birthday Photo Cakes'), ('BC', '1st Birthday Cakes'), ('SBC', 'Special Birthday Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.CharField(choices=[('TC', 'Tea Cakes & Cookies'), ('PC', 'Photo Cakes'), ('Wed', 'Wedding Cakes'), ('GH', 'Gift Hampers'), ('GC', 'Gourmet Cakes'), ('EC', 'Eggless Cakes'), ('HC', 'Heart-Shaped Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='design',
            name='designing',
            field=models.CharField(choices=[('CTC', 'Cricket Theme Cakes'), ('ANC', 'Alphabet & Number Cakes'), ('BSC', 'Baby Shower Cakes'), ('JTC', 'Jungle Theme Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='dessert_cake',
            name='dessert_cake',
            field=models.CharField(choices=[('JC', 'Jar Cakes'), ('BN', 'Brownies'), ('PS', 'Pastries'), ('CC', 'Cup Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='flavour',
            name='flavour',
            field=models.CharField(choices=[('CC', 'Chocolate Cakes'), ('PC', 'Pineapple Cakes'), ('RC', 'Red Velvet Cakes'), ('SC', 'Strawberry Cakes'), ('BSC', 'Butterscotch Cakes'), ('BC', 'Blackforest Cakes'), ('FC', 'Fruit Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='kids',
            name='kids',
            field=models.CharField(choices=[('CTC', 'Cartoon Cakes'), ('SHC', 'SuperHero Cakes'), ('CC', 'Car Cakes'), ('PC', 'Princess Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='occasional',
            name='occasion',
            field=models.CharField(choices=[('DC', 'Doctors Dya Cake'), ('TC', 'Teachers Day Cake'), ('MFC', 'Mothers & Fathers Day Cakes')], max_length=3),
        ),
        migrations.AlterField(
            model_name='trend',
            name='trending',
            field=models.CharField(choices=[('SCB', 'Suprise Cake Box'), ('BC', 'Bomb Cakes'), ('PC', 'Pinata Cakes'), ('PMC', 'Pull Me Up Cakes')], max_length=3),
        ),
    ]
