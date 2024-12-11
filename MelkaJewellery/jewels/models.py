from MelkaJewellery.jewels.choices import JewelryChoices
from django.db import models
from cloudinary.models import CloudinaryField


class CategoryJewel(models.Model):
    type = models.CharField(
        max_length=30,
        choices=JewelryChoices.choices,
        default=JewelryChoices.EARRINGS,
    )


class Collection(models.Model):
    caption = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.PositiveIntegerField(default=0)


class Jewels(models.Model):
    image = CloudinaryField('image', blank=True, null=True)

    type = models.ForeignKey(
        to=CategoryJewel,
        on_delete=models.CASCADE,
    )
    collection = models.OneToOneField(
        to=Collection,
        on_delete=models.CASCADE,
        default=1,
    )
