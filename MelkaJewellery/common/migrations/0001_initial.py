# Generated by Django 5.1.4 on 2024-12-11 18:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.RegexValidator('^[A-Za-z]+$', message='Your name must contain letters only!')])),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=255)),
            ],
        ),
    ]