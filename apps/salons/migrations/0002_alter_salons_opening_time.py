# Generated by Django 4.2.7 on 2023-11-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salons',
            name='opening_time',
            field=models.CharField(max_length=250),
        ),
    ]
