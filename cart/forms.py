from django import forms

QUANTITY_CHOICE_LEN = [(i, str(i)) for i in range(1, 21)]

class AddToCartForm(forms.Form):

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICE_LEN, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)