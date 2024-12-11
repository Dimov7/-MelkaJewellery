from django.db import models


class JewelryChoices(models.TextChoices):
    EARRINGS = 'EARRINGS', 'Earrings'
    BRACELET = 'BRACELET', 'Bracelet'
    NECKLACE = 'NECKLACE', 'Necklace'
    COMBO = 'COMBO', 'Combo'
