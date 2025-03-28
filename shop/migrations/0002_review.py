# Generated by Django 5.1.7 on 2025-03-24 09:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата отзыва')),
                ('vk_avatar_url', models.URLField(blank=True, null=True, verbose_name='Аватар ВКонтакте')),
                ('vk_discussion_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на обсуждение')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
