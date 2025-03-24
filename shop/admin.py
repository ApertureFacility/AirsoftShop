from django.contrib import admin
from .models import Service,Review
from django.contrib import admin


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'date')
    search_fields = ('author', 'text')
    fields = ('author', 'text', 'date')

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
    