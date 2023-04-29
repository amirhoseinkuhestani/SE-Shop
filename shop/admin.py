from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title","is_active"]
    search_fields = ["title"]
    list_filter = ["is_active"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","is_active","price","discount","discount_price","category"]
    search_fields = ["title","note"]
    list_filter = ["is_active","category"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User)
admin.site.register(Admin)