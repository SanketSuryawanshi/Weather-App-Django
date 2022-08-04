from django import forms

class CityData(forms.Form):
    dcity = forms.CharField(max_length=30, required=False)