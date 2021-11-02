from django import forms
from .models import Order

class CreateOrderForm(forms.ModelForm):

  class Meta:
    model = Order
    fields = ['first_name', 'last_name', 'email',
    'address', 'city', 'postal_code']
    widgets = {
      'first_name': forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': 'نام خود را وارد کنید'}),
      'last_name': forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': 'فامیلی خود را وارد کنید'}),
      'email': forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': 'آدرس ایمیل خود را وارد کنید'}),
      'address': forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': 'آدرس کامل خود را وارد کنید'}),
      'city': forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': 'نام شهر خود را وارد کنید'}),
      'postal_code': forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': 'کد پستی خود را وارد کنید'})
    }
    labels = {
      'first_name': 'نام',
      'last_name': 'فامیلی',
      'email': 'ایمیل',
      'address': 'آدرس کامل',
      'city': 'شهر',
      'postal_code': 'کد پستی'
    }