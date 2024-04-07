from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    Username = None
    email = models.EmailField(max_length=50, unique=True, verbose_name='почта', help_text='введите почту')
    token = models.CharField(max_length=50, verbose_name='токен', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
