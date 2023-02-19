from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from .models import MyUser
from .models import Membership


# Create your forms here.

class membershipForm(forms.ModelForm):
    class Meta:
        model=Membership
        fields="__all__"


from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=MyUser
        fields=("Admin","Member","username","first_name","last_name","email")

class MyUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model=MyUser
        fields=("Admin","Member","username","first_name","last_name","email")