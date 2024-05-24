import smtplib
from datetime import datetime, timedelta

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django.core.mail import send_mail

from mailing.models import SubscribeSettings, Logs


# Главная функция по отправке рассылки
def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings_update_status = (SubscribeSettings.objects.filter(start_time__lte=current_datetime)
                .filter(status__in=['created', 'started']))

    for mailing in mailings_update_status:
        if mailing.end_time < current_datetime:
            mailing.status = 'completed'
            mailing.save()

    mailings = (SubscribeSettings.objects.filter(is_active=True).filter(start_time__lte=current_datetime).
                filter(end_time__gte=current_datetime).filter(status__in=['created', 'started']))

    mailing_list = []

    for mailing in mailings:

        if mailing.next_run is None:
            mailing_list.append(mailing)
        elif mailing.next_run < current_datetime:
            mailing_list.append(mailing)

    for mailing in mailing_list:
        try:
            send_mail(
                    subject=mailing.message.title,
                    message=mailing.message.text,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email for client in mailing.client.all()]
               )
            status = True
            response_server = 'Успешно'
        except smtplib.SMTPResponseException as error:
            status = False
            response_server = str(error)
        finally:
            Logs.objects.create(time=current_datetime, status=status, response_server=response_server, message=mailing)

        if mailing.frequency == 'daily':
            mailing.next_run = current_datetime + timedelta(days=1)
        elif mailing.frequency == 'weekly':
            mailing.next_run = current_datetime + timedelta(days=7)
        elif mailing.frequency == 'monthly':
            mailing.next_run = current_datetime + timedelta(days=30)
        mailing.save()


# Функция старта периодических задач
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, 'interval', seconds=1)
    scheduler.start()
