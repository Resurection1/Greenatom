from django.contrib import admin

from api.models import User, Message


@admin.register(User)
class TagAdmin(admin.ModelAdmin):
    """Класс настройки раздела тегов."""

    list_display = (
        'id',
        'username',

    )
    list_display_links = ('id', 'username',)
    empty_value_display = 'значение отсутствует'
    search_fields = ('name',)


@admin.register(Message)
class TagAdmin(admin.ModelAdmin):
    """Класс настройки раздела тегов."""

    list_display = (
        'id',
        'sender',
        'recipient',
        'text',
        'timestamp',
    )
    list_display_links = ('id', 'sender',)
    empty_value_display = 'значение отсутствует'
