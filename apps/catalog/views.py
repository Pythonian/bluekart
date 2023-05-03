from django.shortcuts import get_object_or_404, render

from apps.cart.forms import CartAddProductForm

from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    template = 'catalog/product_list.html'
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }

    return render(request, template, context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    template = 'catalog/product_detail.html'
    context = {
        'cart_product_form': cart_product_form,
        'product': product
    }

    return render(request, template, context)