from MelkaJewellery.common import views
from MelkaJewellery.common.views import AccountCreateView, ProfileDetailView, ProfileUpdateView, AccountDeleteView
from django.contrib.auth.views import LogoutView
from django.urls import path, include

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('contact-page/', views.ContactPage.as_view(), name='contact-page'),
    path('shop/', views.ShopPageView.as_view(), name='shop'),
    path('register/', AccountCreateView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('details/', ProfileDetailView.as_view(), name='profile-details'),
    path('edit/', ProfileUpdateView.as_view(), name='profile-update'),
    path('delete/', AccountDeleteView.as_view(), name='profile-delete'),
]
