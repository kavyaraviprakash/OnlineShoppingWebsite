from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'update_at', 'status']
    readonly_fields = ('name', 'subject', 'email', 'message', 'ip')
    list_filter = ['status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'price', 'available', 'image_tag']
    list_filter = ['category', 'available']
    readonly_fields = ('image_tag',)
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'quantity', 'price', 'total']
    list_filter = ['customer']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'shipping', 'cart_total', 'cart_items', 'complete']
    list_filter = ['complete']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'address', 'city', 'state']
    list_filter = ['customer', 'city', 'state']


# Not used in the project
class Category2Admin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Category2, Category2Admin)
