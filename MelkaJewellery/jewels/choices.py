from django.db import models


class JewelryChoices(models.TextChoices):
    EARRINGS = "ОБЕЦИ", "ОБЕЦИ"
    BRACELET = "ГРИВНИ", "ГРИВНИ"
    NECKLACE = "КОЛИЕТА", "КОЛИЕТА"
    COMBO = "КОМПЛЕКТИ", "КОМПЛЕКТИ"


class SeasonChoices(models.TextChoices):
    SPRING = "ПРОЛЕТ", "ПРОЛЕТ"
    SUMMER = "ЛЯТО", "ЛЯТО"
    FALL = "ЕСЕН", "ЕСЕН"
    WINTER = "ЗИМА", "ЗИМА"


class CollectionChoices(models.TextChoices):
    AMALFI_2024 = 'AMALFI-2024', 'AMALFI-2024'
    AMALFI_2025 = 'AMALFI-2025', 'AMALFI-2025'
    XOXO = 'XO-XO', 'XO-XO'
    XOXO_SNOW = 'XO-XO SNOW', 'XO-XO SNOW'
