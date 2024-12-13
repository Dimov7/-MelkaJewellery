# Generated by Django 5.1.4 on 2024-12-11 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewels', '0006_collection_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='name',
            new_name='caption',
        ),
        migrations.RenameField(
            model_name='collection',
            old_name='season',
            new_name='short_description',
        ),
        migrations.AlterField(
            model_name='categoryjewel',
            name='type',
            field=models.CharField(choices=[('EARRINGS', 'Earrings'), ('BRACELET', 'Bracelet'), ('NECKLACE', 'Necklace'), ('COMBO', 'Combo')], default='EARRINGS', max_length=30),
        ),
    ]
