from django.db import models
from django.shortcuts import render


class Blog(models.Model):
    """класс для создания модели блога"""
    title = models.CharField(max_length=100, verbose_name='заголовок')
    text = models.TextField(verbose_name='содержимое статьи')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', null=True, blank=True)
    count_views = models.IntegerField(default=0, verbose_name='количество просмотров')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
