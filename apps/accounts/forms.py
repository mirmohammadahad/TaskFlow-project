
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class TaskFlowLoginForm(AuthenticationForm):
    """
    Custom login form with email and password fields.
    """

    username = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email",
            "autocomplete": "email",
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your password",
            "autocomplete": "current-password",
        })
    )
