# Generated by Django 4.2.5 on 2023-09-27 12:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to='icons', validators=[django.core.validators.FileExtensionValidator(['svg'])]),
        ),
    ]
