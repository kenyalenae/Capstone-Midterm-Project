# Generated by Django 2.1.2 on 2018-10-18 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
