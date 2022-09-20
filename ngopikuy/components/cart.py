from itertools import product
from django_unicorn.components import UnicornView, QuerySetType
from ngopikuy.models import Cart
from django.db.models import F

class CartView(UnicornView):
    user_products: QuerySetType[Cart] = None
    user_pk: int
    total : float = 0
    qty : int = 0

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.user_products = Cart.objects.filter(user=self.user_pk)
        self.get_total()

    def add_item(self, product_pk):
        item, created = Cart.objects.get_or_create(user_id=self.user_pk, product_id = product_pk)
        if not created:
            item.quantity = F('quantity') + 1
            item.save()
            
        self.user_products = Cart.objects.filter(user=self.user_pk)
        self.get_total()

    def subtract_item(self, product_pk):
        item = Cart.objects.get(user_id=self.user_pk, product_id = product_pk)
        if item is not None:
            if item.quantity == 1:
                item.delete()
            else:
                item.quantity = F('quantity') - 1
                item.save()
                
        self.user_products = Cart.objects.filter(user=self.user_pk)
        self.get_total()
       

    def delete_item(self, product_pk):
        item = Cart.objects.filter(pk=product_pk)
        item.delete()
        self.user_products = self.user_products.exclude(pk=product_pk)
        self.get_total()

    def get_total(self):
        self.qty=0
        for item in self.user_products:
            self.qty = self.qty + item.quantity
        self.total = sum(product.totalPrice for product in self.user_products)/1000.0
