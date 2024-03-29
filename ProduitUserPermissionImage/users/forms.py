from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email']