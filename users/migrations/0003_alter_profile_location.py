# Generated by Django 5.0 on 2024-01-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_itempictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='Location', max_length=100),
        ),
    ]