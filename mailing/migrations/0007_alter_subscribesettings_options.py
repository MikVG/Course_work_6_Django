# Generated by Django 4.2.2 on 2024-05-18 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0006_client_owner_message_owner_subscribesettings_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribesettings',
            options={'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
    ]
