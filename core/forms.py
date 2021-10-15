from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.base import Model
from django.forms import fields
from django.http.request import validate_host

class LoginForm(forms.Form):

  username = forms.CharField(max_length=50, label="نام کاربری", widget=forms.TextInput(attrs={
    'name':'username', 'id':'username', 'placeholder':'نام کاربری خود را وارد کنید', 'class':'form-control my-2'
  }))
  password = forms.CharField(max_length=50, label="رمز عبور", widget=forms.PasswordInput(attrs={
    'name':'password', 'id':'password', 'placeholder':'گذرواژه خود را وارد کنید', 'class':'form-control my-2'
  }))




class RegisterForm(forms.ModelForm):


  username = forms.CharField(min_length=5, max_length=50, label="نام کاربری", widget=forms.TextInput(attrs={
    'name':'username', 'id':'username', 'placeholder':'نام کاربری خود را وارد کنید', 'class':'form-control my-2'
  }))
  email = forms.CharField(min_length=5, max_length=50, label="ایمیل", widget=forms.TextInput(attrs={
    'name':'email', 'id':'email', 'placeholder':'آدرس الکترونیک خود را وارد کنید', 'class':'form-control my-2'
  }))
  password = forms.CharField(max_length=50, label="رمز عبور", widget=forms.PasswordInput(attrs={
    'name':'password', 'id':'password', 'placeholder':'گذرواژه خود را وارد کنید', 'class':'form-control my-2'
  }))
  password2 = forms.CharField(max_length=50, label="تکرار رمز عبور", widget=forms.PasswordInput(attrs={
    'name':'password2', 'id':'password2', 'placeholder':'تکرار گذرواژه خود را وارد کنید', 'class':'form-control my-2'
  }))

  class Meta:
    
    model = User
    fields = ('username', 'email', 'password', 'password2')

  def clean_username(self):

    username = self.cleaned_data.get('username').lower()
    new = User.objects.filter(username=username)

    if new.count():
      raise ValidationError('نام کاربری انتخاب شده از قبل در دیتابیس وجود دارد')
    return username

  def clean_email(self):

    email = self.cleaned_data.get('email')
    new = User.objects.filter(email=email)

    if new.count():
      raise ValidationError('نام کاربری انتخاب شده از قبل در دیتابیس وجود دارد')
    return email
  
  def clean_password2(self):

    password = self.cleaned_data.get('password')
    password2 = self.cleaned_data.get('password2')

    if password and password2 and password != password2:
      raise ValidationError("رمز عبور با تکرار آن مطابقت ندارد!")

    return password2

  def save(self, commit=True):
    cd = self.cleaned_data
    instance = super().save(commit=False)
    instance.set_password(cd['password'])
    if commit:
      super().save(commit=True)