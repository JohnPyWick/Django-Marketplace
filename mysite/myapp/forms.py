from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'desc', 'price','file']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name','password1','password2']
        