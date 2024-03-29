from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("<slug:slug>/", views.product_detail, name="detail"),
    path("", views.product_list, name="list"),
]
