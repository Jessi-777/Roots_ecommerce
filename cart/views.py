from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.http import HttpResponse



def cart(request):
    return render(request, 'store/cart.html')


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart   


# retrieving the product
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request)) #retrieving cart using the cart_id in current session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        # incrementation cart_item.quantity = cart_item.quantity + 1
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
                cart = cart,
                product = product, 
                quantity = 1,
        )
        cart_item.save()
    return HttpResponse(cart_item.product)
    exit()
    # return redirect('cart')

  

