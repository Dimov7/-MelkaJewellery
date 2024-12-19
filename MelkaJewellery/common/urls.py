from MelkaJewellery.common import views
from django.urls import path

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('contact-page/', views.ContactPage.as_view(), name='contact-page'),
]
