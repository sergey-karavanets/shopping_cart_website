from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'region', 'city',
                    'street_name', 'house_number', 'case_number',
                    'apartment_number', 'postal_code']
    list_filter = ['paid']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
