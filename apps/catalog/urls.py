from django.urls import path

from .views import product_detail, product_list

app_name = 'catalog'

urlpatterns = [
    path('<int:id>/<slug:slug>/',
         product_detail, 
         name='product_detail'),

    path('<slug:category_slug>/',
         product_list,
         name='product_list_by_category'),
    
    path('',
         product_list,
         name='product_list'),
]