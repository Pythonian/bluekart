from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("search/", views.product_search, name="product_search"),
    path("", views.home, name="home"),
]
