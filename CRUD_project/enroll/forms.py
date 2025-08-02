from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'name': 'username'  # Change name attribute
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'name': 'useremail'  # Change name attribute
            }),
            'password': forms.PasswordInput(render_value=True,attrs={
                'class': 'form-control',
                'autocomplete': 'new-password',
                'name': 'userpassword'  # Change name attribute
            }),
        }

