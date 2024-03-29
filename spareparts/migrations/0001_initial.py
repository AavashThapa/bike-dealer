# Generated by Django 3.2.18 on 2023-04-24 15:20

import ckeditor.fields
import datetime
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spareparts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', ckeditor.fields.RichTextField()),
                ('brand', models.CharField(max_length=100)),
                ('compatible_vehicle', models.CharField(max_length=100)),
                ('package_includes', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('stock', models.CharField(choices=[('On Stock', 'On Stock'), ('Selling Fast', 'Selling Fast'), ('Out of Stock', 'Out of Stock')], max_length=100)),
                ('price', models.IntegerField()),
                ('quantity_available', models.IntegerField()),
                ('parts_photo', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=None, size=[768, 768], upload_to='photos/%Y/%m/%d/')),
                ('parts_photo_1', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=None, size=[768, 768], upload_to='photos/%Y/%m/%d/')),
                ('parts_photo_2', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=None, size=[768, 768], upload_to='photos/%Y/%m/%d/')),
                ('parts_photo_3', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=None, size=[768, 768], upload_to='photos/%Y/%m/%d/')),
                ('parts_photo_4', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=None, size=[768, 768], upload_to='photos/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Sparepart',
                'verbose_name_plural': 'Spareparts',
            },
        ),
    ]
