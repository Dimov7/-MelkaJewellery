from django.urls import path

from MelkaJewellery.jewels import views
from MelkaJewellery.jewels.views import JewelDeleteView

urlpatterns = [
    path('', views.ShopPageView.as_view(), name='shop'),
    path('create/', views.CreateJewelView.as_view(), name='create-jewel'),
    path('edit/<int:pk>/', views.JewelCollectionEditView.as_view(), name='edit-jewel'),
    path('delete/<int:pk>/', JewelDeleteView.as_view(), name='delete-jewel'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]
