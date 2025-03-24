from django.db import models
from django.utils import timezone
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    author = models.CharField("Автор", max_length=100)
    author_avatar = models.URLField("Аватар автора", max_length=500, blank=True, null=True)
    text = models.TextField("Текст отзыва")
    date = models.DateTimeField("Дата отзыва", default=timezone.now)
    vk_post_id = models.CharField("ID поста ВКонтакте", max_length=50, unique=True, blank=True, null=True)
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
    likes_count = models.PositiveIntegerField("Лайки", default=0)
    is_approved = models.BooleanField("Одобрен", default=False)
    
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
    is_active = models.BooleanField('Активно', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'