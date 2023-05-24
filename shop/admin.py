from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title","is_active"]
    search_fields = ["title"]
    list_filter = ["is_active"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","is_active","price","discount","discount_price","category"]
    search_fields = ["title","note"]
    list_filter = ["is_active","category"]


class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
    (None, {'fields': ('username', 'email', 'phone_number', 'password')}),
    ('Personal info', {'fields': ('first_name', 'last_name', 'iban', 'national_id')}),
    ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'username', 'phone_number')
    ordering = ('email',)
    filter_horizontal = ()


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'notification_type')
    list_filter = ('notification_type',)
    search_fields = ('user__username', 'user__email', 'message')
    readonly_fields = ('created_at',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Notification, NotificationAdmin)
