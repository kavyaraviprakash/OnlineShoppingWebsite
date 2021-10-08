from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CartAddProductForm(forms.Form):
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)