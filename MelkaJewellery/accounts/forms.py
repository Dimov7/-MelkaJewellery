from django.contrib.auth import get_user_model

from MelkaJewellery.accounts.models.profile import Profile

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, SetPasswordMixin
from django import forms

UserModel = get_user_model()


class AccountCreationForm(UserCreationForm):
    password1, password2 = SetPasswordMixin.create_password_fields()

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ("username", "email",)
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Име"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Парола",
        })
        self.fields['password2'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Повтори парола",
        })


class CustomLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Име', "autofocus": True}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Парола', "autocomplete": "current-password"}),
    )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'age': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Profile Image'}),
        }
