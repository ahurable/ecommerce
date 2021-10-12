from django.urls import path
from .views import ProductDetail

urlpatterns = [
    path('product/<int:id>', ProductDetail.as_view(), name="product_detail_url")
]
