# Generated by Django 4.0.6 on 2024-03-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('letter', 'letter'), ('phone_model', 'phone_model')], max_length=100),
        ),
    ]
