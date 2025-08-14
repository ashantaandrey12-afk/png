from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User