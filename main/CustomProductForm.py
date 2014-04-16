from django import forms

class CustomProductForm(forms.Form):
    url = forms.CharField()
    itemname = forms.CharField()
    brand = forms.CharField()
    price = forms.FloatField()
    category = forms.CharField()
    description = forms.CharField()