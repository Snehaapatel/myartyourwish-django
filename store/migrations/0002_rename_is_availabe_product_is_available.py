# Generated by Django 4.0.6 on 2024-02-08 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_availabe',
            new_name='is_available',
        ),
    ]
