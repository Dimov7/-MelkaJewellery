# Generated by Django 5.1.4 on 2024-12-10 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewels', '0005_alter_jewels_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
