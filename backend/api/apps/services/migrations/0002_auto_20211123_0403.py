# Generated by Django 3.0.8 on 2021-11-23 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='approved_provider',
            new_name='approved_providers',
        ),
    ]