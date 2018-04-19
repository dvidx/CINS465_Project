from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

import datetime


class Survey_Form(forms.Form):
    survey_name = forms.CharField(label='Survey', required=True, max_length=120) #validators=[validate_slug],
    survey_creation = forms.DateField(label='Creation', initial=datetime.date.today)
    survey_size = forms.IntegerField(label='Size')
    survey_description = forms.CharField(label='Description',required=True, max_length=240)

class Event_Form(forms.Form):
    name = forms.CharField(label='Event', max_length=20, required=True)
    start_date = forms.DateField(label='Start Date', required=True)
    end_date = forms.DateField(label='End Date', required=True)
    location = forms.CharField(label='Location', max_length=50)
    description = forms.CharField(label='Description', max_length=240)
    image = forms.ImageField(label='Image')

class LoginForm(AuthenticationForm):
    username=forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={
            'name':'username'
        })
    )
    password=forms.CharField(
        label="Password",
        max_length=32,
        widget=forms.PasswordInput()
    )

class registration_form(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email",
            "password1", "password2")

    def save(self, commit=True):
        user=super(registration_form,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user
