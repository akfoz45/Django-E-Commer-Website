from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label="Number", initial=1, widget=forms.NumberInput(attrs={'class': 'form-control me-3', 'id': 'inputQuantity', 'style': 'max-width: 5rem'}))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)