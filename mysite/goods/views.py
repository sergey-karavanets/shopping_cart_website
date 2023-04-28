from django.shortcuts import render, get_object_or_404, get_list_or_404
from cart.forms import CartAddProductForm
from .models import Product


def product_list(request):
    products = get_list_or_404(Product)
    return render(request, 'goods/product/list.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'goods/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
