# Generated by Django 3.2.8 on 2021-10-08 16:50

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_active'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('custom_object', django.db.models.manager.Manager()),
            ],
        ),
    ]
