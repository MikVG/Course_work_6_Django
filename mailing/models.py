from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    """
    класс для описания модели клиента сервиса
    """
    email = models.EmailField(max_length=50, verbose_name='контактный email')
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.email} {self.fio}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    """
    класс для описания модели сообщения
    """
    title = models.CharField(max_length=100, verbose_name='тема рассылки')
    text = models.TextField(verbose_name='текст рассылки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class SubscribeSettings(models.Model):
    """
    класс для описания модели настроек рассылки
    """

    FREQUENCY_CHOICES = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    start_time = models.DateTimeField(verbose_name='время начала рассылки')
    end_time = models.DateTimeField(verbose_name='время окончания рассылки')
    next_run = models.DateTimeField(verbose_name='дата и время следующей рассылки', blank=True, null=True)
    frequency = models.CharField(max_length=25, verbose_name='периодичность рассылки', choices=FREQUENCY_CHOICES,
                                 default='daily')
    status = models.CharField(max_length=25, verbose_name='статус рассылки', choices=STATUS_CHOICES,
                              default='created')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')
    client = models.ManyToManyField(Client, verbose_name='клиент', blank=True)


class Logs(models.Model):
    """
    класс для описания модели логирования
    """
    time = models.DateTimeField(verbose_name='дата и время последней попытки')
    status = models.BooleanField(verbose_name='статус попытки')
    response_server = models.CharField(max_length=150, verbose_name='ответ почтового сервера', **NULLABLE)
    message = models.ForeignKey(SubscribeSettings, on_delete=models.CASCADE, verbose_name='рассылка')

    def __str__(self):
        return f'{self.time} {self.status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
