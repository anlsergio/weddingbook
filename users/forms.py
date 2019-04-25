from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# This is where you can define your own custom form to include in the view
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Define the new property and its rules

    class Meta:
        model = User # Model to be affected
        fields = [ # Fields you want to be displayed
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]
