from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Order, OrderItem


def order_stripe_payment(obj):
    url = obj.get_stripe_url()
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ''
order_stripe_payment.short_description = 'Stripe payment'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'address', 'paid', order_stripe_payment, 'created']
    list_filter = ['paid', 'created']
    inlines = [OrderItemInline]