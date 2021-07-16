# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age',) # previously we use "UserCreationForm.Meta.fields + ('age',)"
                                               # for our fields but now we add the exact fields that we wanted.


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age',) # previously we use "UserChangeForm.Meta.fields"
                                               # for our fields but now we add the exact fields that we wanted.