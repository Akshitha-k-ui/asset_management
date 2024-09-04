# Generated by Django 5.1 on 2024-09-01 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_asset_id_asset_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='Id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='asset',
            name='purchased_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
