# Generated by Django 5.1.4 on 2024-12-11 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_emailfieldmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
