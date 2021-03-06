from django.contrib.auth.models import User
from django import forms

class SignUpForm(forms.ModelForm):

    password = forms.CharField(label = 'Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        # fill out fields with values for signup
        # can be added another field
        fields = ['username', 'password', 'first_name', 'last_name', 'email',]