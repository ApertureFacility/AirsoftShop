from django.db import models

class Service(models.Model):
    SERVICE_TYPES = (
        ('AEG', 'Электрические приводы'),
        ('GBB', 'Газовые приводы'),
        ('UPG', 'Апгрейды'),
    )
    
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)
    image = models.ImageField('Изображение', upload_to='services/')
    service_type = models.CharField('Тип услуги', max_length=3, choices=SERVICE_TYPES)
    is_active = models.BooleanField('Активно', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'