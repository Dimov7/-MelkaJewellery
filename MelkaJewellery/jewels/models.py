from MelkaJewellery.jewels.choices import JewelryChoices, SeasonChoices, CollectionChoices
from django.db import models
from cloudinary.models import CloudinaryField


class CategoryJewel(models.Model):
    type = models.CharField(
        max_length=30,
        choices=JewelryChoices.choices,
        default=JewelryChoices.EARRINGS,
    )

    def __str__(self):
        return self.type


class CollectionJewel(models.Model):
    collection = models.CharField(
        max_length=30,
        choices=CollectionChoices.choices,
        default=CollectionChoices.AMALFI_2024
    )

    def __str__(self):
        return self.collection


class SeasonsJewel(models.Model):
    season = models.CharField(
        max_length=50,
        choices=SeasonChoices.choices,
        default=SeasonChoices.SUMMER,
    )

    def __str__(self):
        return self.season


class Collection(models.Model):
    caption = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=2000, blank=True, null=True)
    materials_used = models.CharField(max_length = 2000, blank=True, null=True)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.caption


class Jewels(models.Model):
    image = CloudinaryField('image', blank=True, null=True)

    additional_image_1 = CloudinaryField('image', blank=True, null=True)
    additional_image_2 = CloudinaryField('image', blank=True, null=True)

    type = models.ForeignKey(
        to=CategoryJewel,
        on_delete=models.CASCADE,
    )
    collection = models.OneToOneField(
        to=Collection,
        on_delete=models.CASCADE,
        default=1,
    )
    season_jewel = models.ForeignKey(
        to=SeasonsJewel,
        on_delete=models.CASCADE,
    )

    collection_jewel = models.ForeignKey(
        to=CollectionJewel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.image
