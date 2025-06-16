from django import forms
from django.contrib.auth.forms import AuthenticationForm

class EmailLoginForm(AuthenticationForm):
  username = forms.CharField(
    label="Email",
    widget=forms.EmailInput(attrs={
      'class': 'form-control',
      'placeholder': 'Enter your email',
      'autocomplete': 'email',
      'autocapitalize': 'none',
      'inputmode': 'email',
    })
  )
  password = forms.CharField(
    label="Password",
    widget=forms.PasswordInput(attrs={
      'class': 'form-control',
      'placeholder': 'Enter your password',
      'autocomplete': 'current-password',
    })
  )
