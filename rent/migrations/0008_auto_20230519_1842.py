# Generated by Django 3.0.7 on 2023-05-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0007_auto_20230517_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rentreview',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
