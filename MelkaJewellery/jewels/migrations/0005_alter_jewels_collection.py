# Generated by Django 5.1.4 on 2024-12-10 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewels', '0004_alter_jewels_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewels',
            name='collection',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='jewels.collection'),
        ),
    ]
