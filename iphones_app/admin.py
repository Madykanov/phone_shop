from django.contrib import admin
from .models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email',]

admin.site.register(Contact,ContactAdmin)


admin.site.register(Brand)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','brand','price','quant','color']
    list_filter = ('brand','color')
    search_fields = ('title','brand','color')

admin.site.register(Product,ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'price']
    list_filter=("product",)
    search_fields = ("user", "product")

admin.site.register(Cart, CartAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price']
    list_filter=("product",)
    search_fields = ("user", "product")

admin.site.register(Order, OrderAdmin)


admin.site.register(Favorite)


class OpinionAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
    list_filter=('user', 'product')

admin.site.register(Opinion,OpinionAdmin)

