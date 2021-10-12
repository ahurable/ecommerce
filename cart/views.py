from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.decorators.http import require_POST
from .cart import Cart
from shop.models import Product
from .forms import AddToCartForm

# Create your views here.

@require_POST
def AddToCartView(request, id):

  product = get_object_or_404(Product, id=id)
  cart = Cart(request)
  form = AddToCartForm(request.POST)

  if form.is_valid():
    cd = form.cleaned_data
    cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('home_url')


@require_POST
def RemoveFromCart(request, product_id):

  product = get_object_or_404(Product, id=product_id)
  cart = Cart(request)
  cart.remove(product=product)
  return redirect(request, 'cart:cart_detail_url')

def CartDetail(request):
  
  is_product = False
  cart = Cart(request)
  return render(request, 'cart/cart.html', context={'cart':cart, 'is_product': is_product})