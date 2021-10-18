from .cart import Cart

def cart(request):
  cart = Cart(request)
  cart_len = cart.get_len_of_whole()
  return {'cart':cart, 'cart_len': cart_len}