from django.db import models
from store.models import Product

class Cart(models.Model):
    date_added = models.DateField(auto_now_add=True)
    cart_id = models.CharField(max_length=250, blank=True)
    

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    # user = models.ForeignKey()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product

    def sub_total(self):
        return self.product.price * self.quantity

