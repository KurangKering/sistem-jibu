from django import forms

class DataUjiForm(forms.Form):
    raw_data = forms.CharField(max_length=400)
