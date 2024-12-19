from MelkaJewellery.common.models import ContactPageModel
from django.forms import ModelForm, TextInput, EmailInput

from django.contrib.auth import get_user_model
from django import forms

UserModel = get_user_model()


class ContactPageForm(ModelForm):
    class Meta:
        model = ContactPageModel
        fields = ['name', 'email', 'message']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Име'}),
            'email': EmailInput(attrs={'placeholder': 'Имейл'}),
            'message': TextInput(attrs={'placeholder': 'Съобщение'})
        }


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Търси...',
        })
    )
