# Generated by Django 4.2.2 on 2024-05-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0009_subscribesettings_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribesettings',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активность'),
        ),
    ]
