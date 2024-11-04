from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс пользователя."""

    friends = models.ManyToManyField(
        'self', symmetrical=False, related_name='friend_of', blank=True)

    def add_friend(self, friend_username):
        friend = User.objects.get(username=friend_username)
        if friend and friend != self:
            self.friends.add(friend)
            friend.friends.add(self)
            return True
        return False

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Message(models.Model):
    """Класс сообщений."""

    sender = models.ForeignKey(
        User,
        related_name='sent_messages',
        on_delete=models.CASCADE,
        verbose_name='Отправитель',
    )
    recipient = models.ForeignKey(
        User,
        related_name='received_messages',
        on_delete=models.CASCADE,
        verbose_name='Получатель',
    )
    text = models.TextField(
        verbose_name='Текст',
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Временная метка'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.sender} to {self.recipient}: {self.text}'
