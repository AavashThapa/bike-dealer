# Generated by Django 3.0.7 on 2023-05-12 12:14

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0007_auto_20230511_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[], max_length=200),
        ),
    ]
