# Generated by Django 3.0.6 on 2022-05-14 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0009_remove_flete_vehiculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='flete',
            name='vehiculo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='vehiculo.Transport'),
            preserve_default=False,
        ),
    ]