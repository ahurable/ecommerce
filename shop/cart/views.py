from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import override
from django.views.generic import View
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from .cart import Cart
from shop.models import Product
from .forms import AddToCartForm

# Create your views here.

def AddToCartView(request, id):

  product = get_object_or_404(Product, id=id)
  cart = Cart(request)
  
  if request.method == "POST":
    form = AddToCartForm(request.POST)
    if form.is_valid():
      print("form validate")
      cd = form.cleaned_data
      cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
      return redirect('cart_detail_url')
  else:
    cart.add(product=product, override_quantity=True)
    cart_len = cart.get_len_of_whole()
    return JsonResponse({'say':f'شما {cart_len} آیتم در سبد خرید خود دارید  <a href=''/cart/cartdetail''>مشاهده سبد خرید و ادامه برای پرداخت</a> گزینه های انتخاب شده.'}, status=200)



@require_POST
def RemoveFromCart(request, product_id):

  product = get_object_or_404(Product, id=product_id)
  cart = Cart(request)
  cart.remove(product=product)
  return redirect('cart_detail_url')


def CartDetail(request):
    cart = Cart(request)
    total_price = cart.get_total_price()
    return render(request, 'cart/cart.html', {'cart': cart, 'total_price': total_price})