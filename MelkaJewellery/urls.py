from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MelkaJewellery.common.urls')),
    path('accounts/', include('MelkaJewellery.accounts.urls')),
    path('shop/', include('MelkaJewellery.jewels.urls')),

]
