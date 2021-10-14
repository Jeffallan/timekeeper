# Generated by Django 3.0.8 on 2021-02-02 03:29

import api.apps.core.util.users
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, api.apps.core.util.users.UserChoice['Maintenance']), (2, api.apps.core.util.users.UserChoice['Operator']), (3, api.apps.core.util.users.UserChoice['Audience'])], default=3),
        ),
    ]
