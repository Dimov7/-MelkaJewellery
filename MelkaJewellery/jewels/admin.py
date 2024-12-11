from django.contrib import admin

# Register your models here.

from .models import Jewels, Collection, CategoryJewel

admin.site.register(Jewels)
admin.site.register(Collection)
admin.site.register(CategoryJewel)