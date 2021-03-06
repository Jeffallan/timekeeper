# Generated by Django 3.0.8 on 2021-11-23 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20211110_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140, unique=True)),
                ('service_type', models.CharField(choices=[('Hour', 'Hour'), ('Foot', 'Foot'), ('Yard', 'Yard'), ('Mile', 'Mile'), ('Unit', 'Unit')], max_length=25)),
                ('is_duration', models.BooleanField(default=False)),
                ('approved_provider', models.ManyToManyField(to='users.Profile')),
            ],
            options={
                'ordering': ['-created', '-updated'],
                'abstract': False,
            },
        ),
    ]
