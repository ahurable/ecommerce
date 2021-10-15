from django.shortcuts import redirect, render
from shop.models import Product
from django.views.generic import ListView
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import success, error
from .forms import LoginForm, RegisterForm


User = get_user_model


class IndexView(ListView):

    model = Product
    template_name = 'index.html'
    context_object_name = 'products'



def LoginView(request):
    login_form = LoginForm(request.POST or None)
    if request.user.is_authenticated:
        error(request, message="شما از قبل وارد سایت شده اید", extra_tags="danger")
        return redirect('home_url')
    if request.method == "POST":
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user:
                login(request, user=user)
                success(request, message="شما با موفقیت وارد سایت شدید", extra_tags="success")
                return redirect('home_url')
    return render(request, 'auth/login.html', {'login_form':login_form})



@login_required
def LogoutView(request):
    logout(request)
    success(request, message="با موفقیت از حساب کاربری خود خارج شدید.", extra_tags='success')
    return redirect('home_url')

def RegisterView(request):
    register_form = RegisterForm(request.POST or None)
    if request.user.is_authenticated:
        error(request, message="شما از قبل وارد سایت شده اید", extra_tags="danger")
        return redirect('home_url')
    if request.method == "POST":
        if register_form.is_valid():
            register_form.save(commit=True)
            success(request, message="حساب کاربری شما با موفقیت ایجاد شد!", extra_tags='danger')
            return redirect('home_url')
    return render(request, 'auth/register.html', {'register_form':register_form})

