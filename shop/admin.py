from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_type', 'price', 'is_active')
    list_filter = ('service_type', 'is_active')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'description', 'price')
        }),
        ('Дополнительно', {
            'fields': ('image', 'service_type', 'is_active')
        }),
    )