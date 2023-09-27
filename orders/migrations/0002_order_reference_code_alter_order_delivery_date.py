# Generated by Django 4.2.5 on 2023-09-27 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='reference_code',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 1, 15, 13, 44, 720734)),
        ),
    ]
