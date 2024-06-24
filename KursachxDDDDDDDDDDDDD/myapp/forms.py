from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1')

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')