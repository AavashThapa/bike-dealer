# Generated by Django 3.2.18 on 2023-04-24 19:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts', '0003_sparepartsorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='spareparts',
            name='features',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]