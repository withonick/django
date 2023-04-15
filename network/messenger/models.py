from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['created_at']


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Chat(models.Model):
    message_from = models.ForeignKey(User, related_name="message_from", on_delete=models.RESTRICT)
    message_to = models.ForeignKey(User, related_name="message_to", on_delete=models.RESTRICT)
    message = models.TextField(null=True, blank=True)
    message_img = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
