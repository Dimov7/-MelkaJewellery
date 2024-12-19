from django.contrib import admin

from .models import Jewels, Collection, CategoryJewel, SeasonsJewel, CollectionJewel

admin.site.register(Jewels)
admin.site.register(Collection)
admin.site.register(CategoryJewel)
admin.site.register(SeasonsJewel)
admin.site.register(CollectionJewel)