from decimal import Decimal
from shop.models import Product
from django.conf import settings

class Cart(object):

    # initilize the cart

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_KEY)
        if not cart:
            cart = self.session[settings.CART_SESSION_KEY] = {}
        self.cart = cart

    # when we iterate accross the class the below generator will be called
    def __iter__(self):
        
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    # this method will get our custom items lentgh when we call the len(cart)
    def __len__(self):

        return sum(item['quantity'] for item in self.cart.values())



    def get_total_price(self):

        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())



    def add(self, product, quantity=1, override_quantity=False):

        product_id = str(product.id)
        quantity = quantity

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': '0', 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        
        self.save()

    def print_it(self):
        return self.cart
    
    def remove(self, product):

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()



    def save(self):
        
        # we turn session modified to True to make sure item will gets saved
        self.session.modified = True

    
    def clear(self):

        del self.session[settings.CART_SESSION_KEY]
        self.save()