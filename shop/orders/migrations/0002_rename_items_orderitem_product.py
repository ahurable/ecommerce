# Generated by Django 3.2.8 on 2021-11-02 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='items',
            new_name='product',
        ),
    ]