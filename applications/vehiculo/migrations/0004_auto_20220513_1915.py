# Generated by Django 3.0.6 on 2022-05-14 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_auto_20220513_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flete',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
