from django.contrib.auth.models import User
from django import forms

class SignUpForm(forms.ModelForm):

    password = forms.CharField(label = 'password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label = 'repeat_password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        # fill out fields with values for signup
        # can be added another field
        fields = ['username', 'password','repeat_password', 'first_name', 'last_name', 'email',]

    def clean_Repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Your password is not correct')
        return cd['repeat_password']