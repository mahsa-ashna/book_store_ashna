# Generated by Django 3.0.4 on 2021-09-09 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
