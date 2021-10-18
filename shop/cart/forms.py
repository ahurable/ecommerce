from django import forms

QUANTITY_CHOICE_LEN = [(i, str(i)) for i in range(1, 21)]

class AddToCartForm(forms.Form):

    # def __init__(self, quantity=1):
        
    #     self.quantity = quantity

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICE_LEN, coerce=int, widget=forms.Select(attrs={"id":"selectId", "class":"form-control w-25 mx-3"}), label="تعداد")
    override = forms.BooleanField(required=False, initial=True, widget=forms.HiddenInput)
