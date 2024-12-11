from django.db import models
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class ContactPageModel(models.Model):
    name = models.CharField(max_length=40,
                            validators=[
                                MinLengthValidator(4),
                                RegexValidator(
                                    "^[A-Za-z]+$"
                                    , message="Your name must contain letters only!")
                            ])
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=255)


class EmailFieldModel(models.Model):
    email = models.EmailField(max_length=100)


class ShopPageModel(models.Model):
    pass
