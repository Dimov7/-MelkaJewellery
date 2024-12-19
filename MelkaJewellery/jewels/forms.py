from django import forms
from .models import Jewels, CategoryJewel, CollectionJewel, SeasonsJewel, Collection
from cloudinary.forms import CloudinaryFileField


class JewelsCreateForm(forms.ModelForm):
    image = CloudinaryFileField(required=False)
    additional_image_1 = CloudinaryFileField(required=False)
    additional_image_2 = CloudinaryFileField(required=False)

    type = forms.ModelChoiceField(queryset=CategoryJewel.objects.all(), required=True)
    season_jewel = forms.ModelChoiceField(queryset=SeasonsJewel.objects.all(), required=True)

    class Meta:
        model = Jewels
        fields = ['image', 'additional_image_1', 'additional_image_2', 'type', 'season_jewel',
                  'collection_jewel']

    widgets = {
        'image': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        'additional_image_1': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        'additional_image_2': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
    }


class JewelCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['caption', 'short_description', 'description', 'materials_used', 'price']

        widgets = {
            'caption': forms.TextInput(attrs={'placeholder': 'Collection Name'}),
            'short_description': forms.TextInput(attrs={'placeholder': 'Short Description'}),
            'description': forms.Textarea(attrs={'placeholder': 'Detailed Description'}),
            'materials_used': forms.Textarea(attrs={'placeholder': 'Materials Used'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }
