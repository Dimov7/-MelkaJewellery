# Generated by Django 5.1.4 on 2024-12-10 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryJewel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('EARRINGS', 'Earrings'), ('BRACELET', 'Bracelet'), ('NECKLACE', 'Necklace')], default='EARRINGS', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Jewels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewels.categoryjewel')),
            ],
        ),
    ]
