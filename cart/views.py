from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import override
from django.views.generic import View
from django.views.decorators.http import require_POST
from .cart import Cart
from shop.models import Product
from .forms import AddToCartForm
from asgiref.sync import sync_to_async
# Create your views here.

@require_POST
def AddToCartView(request, id):

  product = get_object_or_404(Product, id=id)
  cart = Cart(request)
  form = AddToCartForm(request.POST)

  if form.is_valid():
    print("form validate")
    cd = form.cleaned_data
    cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart_detail_url')
  else:
    cart.add(product=product, override_quantity=True)
    return redirect('home_url')


@require_POST
def RemoveFromCart(request, product_id):

  product = get_object_or_404(Product, id=product_id)
  cart = Cart(request)
  cart.remove(product=product)
  return redirect('cart_detail_url')

# def add_form_to_items(items):
#   for item in items:
#     item['u_q_form'] = AddToCartForm(initial={'quantity': item['quantity'], 'override':True})
#   return items

# def CartDetail(request):
#   cart = Cart(request)
#   for item in cart:
#     item['u_q_form'] = AddToCartForm(initial={'quantity': item['quantity'], 'override':True})
#   print(cart)
#   cart = request.session[settings.CART_SESSION_KEY]
#   return render(request, 'cart/cart.html', context={'cart':cart})

def CartDetail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})