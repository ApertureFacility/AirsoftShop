from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Review(models.Model):
    author = models.CharField("Автор", max_length=100)
    text = models.TextField("Текст отзыва")
    date = models.DateTimeField("Дата отзыва", default=timezone.now)
    rating = models.PositiveSmallIntegerField(
        "Оценка",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        blank=True,
        null=True
    )
    service = models.ForeignKey(
        'Service',
        on_delete=models.SET_NULL,
        verbose_name="Услуга",
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"Отзыв от {self.author} ({self.date.strftime('%d.%m.%Y')})"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-date']
        
class Service(models.Model):
    SERVICE_TYPES = (
        ('AEG', 'Ремонт'),
        ('GBB', 'Газовые приводы'),
        ('UPG', 'Апгрейды'),
    )
    
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)
    image = models.ImageField('Изображение', upload_to='services/')
    service_type = models.CharField('Тип услуги', max_length=3, choices=SERVICE_TYPES)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    description = models.TextField(
        'Описание',
        validators=[
            MinLengthValidator(250, message='Описание должно содержать минимум 250 символов'),
            MaxLengthValidator(300, message='Описание должно содержать максимум 300 символов')
        ])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'