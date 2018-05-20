from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions

from .models import *

import datetime

class Event_Form(forms.Form):
    name = forms.CharField(label='Event', max_length=20, required=True)
    start_date = forms.DateField(label='Start Date', required=False, initial=datetime.date.today)
    end_date = forms.DateField(label='End Date', required=False, initial=datetime.date.today)
    location = forms.CharField(label='Location', max_length=50, required=False)
    description = forms.CharField(label='Description', max_length=240, required=False)
    image = forms.ImageField(label='Image', required=False)
    # lng = forms.DecimalField(label='Longitude', required=True)
    # lat = forms.DecimalField(label='Latitude', required=True)

class Ticket_Form(forms.Form):
    event = forms.ModelChoiceField(queryset = Event_Model.objects.all(), label='Event', required=True)
    price = forms.DecimalField(label='Initial price', required=True)
    info = forms.CharField(label='Info', max_length=240, required=False)

class Bid_Form(forms.Form):
    bid = forms.DecimalField(label='Your bid', required=True)
    ticket = forms.ModelChoiceField(queryset = Ticket_Model.objects.all(), label='Ticket', required=True)

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

class profil_form(forms.ModelForm):

    picture = forms.ImageField(required=False)

    class Meta:
        model = Profil_Model
        exclude = ("user", "creation")
