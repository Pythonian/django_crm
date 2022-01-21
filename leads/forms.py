from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Lead

User = get_user_model() 

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'age', 'agent', 
                  'phoned', 'source_of_lead', 'additional_files']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
