# Generated by Django 4.2.5 on 2023-09-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(default='', upload_to='icons'),
            preserve_default=False,
        ),
    ]
