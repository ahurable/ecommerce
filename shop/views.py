from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Product
# Create your views here.


class ProductDetail(View):

    def get(self, request, id):

        product = get_object_or_404(Product, id=id)
        context = {'product': product}
        return render(request, "shop/product_detail.html", context)