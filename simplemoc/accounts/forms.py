from django.contrib.auth.forms import UserCreationForm
from django import forms

#
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')

