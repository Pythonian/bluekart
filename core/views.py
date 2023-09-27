from django.shortcuts import render

from products.models import Category, Product
from stats import stats
from .utils import mk_paginator


def home(request):
    featured_products = Product.active.all()[:6]
    categories = Category.objects.all()
    recently_added_products = Product.objects.order_by("-created")[:4]
    recently_sold_products = Product.objects.order_by("-created")[:4]
    top_rated_products = Product.objects.order_by("-created")[:4]
    recommended_products = Product.active.order_by("?")[:6]
    recently_viewed_products = stats.get_recently_viewed(request)

    template = "home.html"
    context = {
        "featured_products": featured_products,
        "categories": categories,
        "recently_added_products": recently_added_products,
        "recently_sold_products": recently_sold_products,
        "top_rated_products": top_rated_products,
        "recommended_products": recommended_products,
        "recently_viewed_products": recently_viewed_products,
    }
    return render(request, template, context)


def category(request):
    return render(request, "category.html")


def product_search(request):
    products = {}
    product_count = 0
    keyword = ""
    if "keyword" in request.GET:
        keyword = request.GET["keyword"]
        if keyword:
            products = Product.objects.filter(name__icontains=keyword)
            product_count = products.count()
            products = mk_paginator(request, products, 5)

    template_name = "products/search.html"
    context = {
        "products": products,
        "product_count": product_count,
        "keyword": keyword,
    }

    return render(request, template_name, context)


def products(request):
    return render(request, "products.html")


def product(request):
    return render(request, "product.html")


def success(request):
    return render(request, "success.html")


def track_order(request):
    return render(request, "track_order.html")


def wishlist(request):
    return render(request, "wishlist.html")


def checkout(request):
    return render(request, "checkout.html")


def compare(request):
    return render(request, "compare.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def profile(request):
    return render(request, "profile.html")


def orders(request):
    return render(request, "orders.html")


def addresses(request):
    return render(request, "addresses.html")


def settings(request):
    return render(request, "settings.html")


def terms(request):
    return render(request, "terms.html")


def faqs(request):
    return render(request, "faqs.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")
