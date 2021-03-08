from django.contrib.auth.models import User
from django import forms

class SignUpForm(forms.ModelForm):

    password = forms.CharField(label = 'Password', widget=forms.PasswordInput)
    Repeat_password = forms.CharField(label = 'Repeat_password', widget=forms.PasswordInput)
    class Meta:
        model = User
        # fill out fields with values for signup
        # can be added another field
        fields = ['username', 'password','Repeat_password', 'first_name', 'last_name', 'email',]

    def clean_Repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['Repeat_password']:
            raise forms.ValidationError('Your password is not correct')
        return cd['Repeat_password']