from django import forms

class BuyForm(forms.Form):
    productId = forms.IntegerField(widget=forms.HiddenInput)
    selectedQuantity = forms.IntegerField(initial=1, label='Quantity')