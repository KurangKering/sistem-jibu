from django import forms

class KosakataForm(forms.Form):
    kata = forms.CharField(max_length=100)
    arti_kata = forms.CharField(max_length=100)