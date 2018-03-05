from django import forms
from django.core.validators import validate_slug

class Suggestion_Form(forms.Form):
    suggestion = forms.CharField(label='Suggestion:', max_length=240)
