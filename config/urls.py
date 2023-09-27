"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("category/", views.category, name="category"),
    # path("search/", views.search, name="search"),
    path("products/", views.products, name="products"),
    path("product/", views.product, name="product"),
    path("tracking/", views.track_order, name="track_order"),
    path("wishlist/", views.wishlist, name="wishlist"),
    # path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("compare/", views.compare, name="compare"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("addresses/", views.addresses, name="addresses"),
    path("settings/", views.settings, name="settings"),
    path("terms/", views.terms, name="terms"),
    path("faqs/", views.faqs, name="faqs"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("success/", views.success, name="success"),
    path("cart/", include("cart.urls", namespace="cart")),
    path("coupons/", include("coupons.urls", namespace="coupons")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("products/", include("products.urls")),
    path("", include("core.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
