# Generated by Django 3.2.18 on 2023-04-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0005_auto_20230425_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]
