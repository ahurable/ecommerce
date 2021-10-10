from django.shortcuts import render
from shop.models import Product
from django.views.generic import ListView

# def IndexView(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'index.html', context)

class IndexView(ListView):

    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

