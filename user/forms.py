from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreateionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
