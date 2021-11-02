from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import CreateOrderForm
from .models import OrderItem
from shop.cart.cart import Cart
from shop.models import Product
# Create your views here.

class CreateOrderView(View):

  def get(self, request):

    form = CreateOrderForm()
    return render(request, 'order.html', context={'form': form})

  def post(self, request):

    cart = Cart(request)
    form = CreateOrderForm(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      for item in cart:
        _product = Product.objects.get(id=item['product_id'])
        OrderItem.objects.create(order=instance, product=_product, quantity=item['quantity'], price=item['price'])
      return HttpResponse('<h1>سفارش شما با موفقیت دریافت شد!</h1>')