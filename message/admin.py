from django.contrib import admin

from message.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    ordering = ('creation_date',)
    search_fields = [
        'message',
    ]
    list_display = [
        'sender',
        'receiver',
        'creation_date',
        'subject',
    ]
    list_filter = (
        'sender', 'receiver',
    )
    autocomplete_fields = (
        'sender', 'receiver',
    )
