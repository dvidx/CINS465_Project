from django import forms
from django.core.validators import validate_slug

import datetime

class Survey_Form(forms.Form):
    survey_name = forms.CharField(label='Survey', max_length=120)
    survey_creation = forms.DateField(label='Creation', initial=datetime.date.today)
    survey_size = forms.IntegerField(label='Size')
