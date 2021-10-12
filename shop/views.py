from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from cart.forms import AddToCartForm
from .models import Product
# Create your views here.


def ProductDetailView(request, id):

    product = get_object_or_404(Product, id=id)
    add_to_cart_form = AddToCartForm()
    context= {'product': product, 'add_to_cart_form': add_to_cart_form}
    return render(request, 'shop/product_detail.html', context=context)