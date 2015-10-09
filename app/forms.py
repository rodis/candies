from django.forms import ModelForm
from django import forms

from app.models import Sweet


class GeoSweetForm(forms.Form):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

class SweetForm(GeoSweetForm):
    sweet = forms.CharField(
        max_length=140,
        label='',
        widget=forms.Textarea(
            attrs={
                'class': "materialize-textarea validate",
                'length': 140,
                'placeholder': "Your sweet here :)",
            }))
