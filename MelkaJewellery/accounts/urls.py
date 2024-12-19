from MelkaJewellery.accounts.views import AccountCreateView, ProfileDetailView, ProfileUpdateView, AccountDeleteView, \
    CustomLoginView
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('register/', AccountCreateView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('details/', ProfileDetailView.as_view(), name='profile-details'),
    path('edit/', ProfileUpdateView.as_view(), name='profile-update'),
    path('delete/', AccountDeleteView.as_view(), name='profile-delete'),
]
