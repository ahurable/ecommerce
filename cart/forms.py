from django import forms

QUANTITY_CHOICE_LEN = [(i, str(i)) for i in range(1, 21)]

class AddToCartForm(forms.Form):

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICE_LEN, coerce=int, widget=forms.NumberInput(attrs={'id':'quantityId'}))
    override = forms.BooleanField(required=False, initial=True, widget=forms.HiddenInput)