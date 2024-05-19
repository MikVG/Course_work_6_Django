from django.contrib import admin

from mailing.models import Client, Message, SubscribeSettings


@admin.register(Client)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'fio',)


@admin.register(Message)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text',)


@admin.register(SubscribeSettings)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time', 'status',)
