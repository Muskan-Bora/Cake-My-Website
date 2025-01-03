# Generated by Django 5.0 on 2024-04-05 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_alter_category_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_title',
            field=models.CharField(default='Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='categories',
            field=models.CharField(choices=[('GH', 'Gift Hampers'), ('GC', 'Gourmet Cakes'), ('Wed', 'Wedding Cakes'), ('PC', 'Photo Cakes'), ('EC', 'Eggless Cakes'), ('TC', 'Tea Cakes & Cookies'), ('HC', 'Heart-Shaped Cakes')], max_length=3),
        ),
    ]
