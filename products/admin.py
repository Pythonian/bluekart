from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category", "available", "created"]
    list_filter = ["available", "created", "category"]
    list_editable = ["available"]
    prepopulated_fields = {"slug": ("name",)}
