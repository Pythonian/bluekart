from decimal import Decimal
from django.conf import settings

from apps.catalog.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        """Initialize the cart with a request object."""
        # store the current session
        self.session = request.session
        # try to get the cart from the current session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            # Save an empty cart in the session
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """Add a product to the cart or update its quantity."""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as modified to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """Remove a product from the cart."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Iterate over the items in the cart and get the products from the db."""
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        # copy the current cart in the cart variable
        cart = self.cart.copy()
        # add the product instances to the cart
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Count all items in the cart."""
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        """return the total cost of the items in the cart."""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        """Remove cart from user session"""
        del self.session[CART_SESSION_ID]
        self.save()