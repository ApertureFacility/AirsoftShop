from django.contrib import admin
from .models import Service, Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'date')
    search_fields = ('author', 'text')
    fields = ('author', 'text', 'date')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_type', 'price')
    list_filter = ('service_type',)  # Исправлено: добавлена запятая
    search_fields = ('title', 'description')
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['description'].help_text = 'Рекомендуемая длина: 100-300 символов'
        return form
    
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'description', 'price')
        }),
        ('Дополнительно', {
            'fields': ('image', 'service_type')
        }),
    )