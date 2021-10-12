from django.urls import path
from .views import (AddToCartView, RemoveFromCart, CartDetail)


urlpatterns = [
    path('add/<int:id>/', AddToCartView, name="add_to_cart_url"),
    path('remove/<int:product_id>', RemoveFromCart, name="remove_from_cart_url"),
    path('cartdetail', CartDetail, name="cart_detail_url"),
]
