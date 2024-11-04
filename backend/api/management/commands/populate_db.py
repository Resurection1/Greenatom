import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import User, Message


class Command(BaseCommand):
    """Класс заполения тестовыми данными"""

    def handle(self, *args, **kwargs):
        self.populate_db()

    def populate_db(self):
        users = self.create_users()
        self.create_friendships(users)
        self.create_messages(users)

    def create_users(self):
        """Создает пользователей"""
        usernames = ['alice', 'bob', 'charlie', 'david', 'eve']
        users = []
        for username in usernames:
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(f'User {username} created.')
            users.append(user)
        return users

    def create_friendships(self, users):
        """Создает друзей"""
        for user in users:
            friends = random.sample(users, k=random.randint(1, len(users) - 1))
            for friend in friends:
                if friend != user:
                    user.add_friend(friend.username)
                    self.stdout.write(
                        f'{user.username} is now '
                        f'friends with {friend.username}')

    def create_messages(self, users):
        """Создает сообщения"""
        messages = [
            "Hello!", "How are you?", "What's up?", "Let's meet up!",
            "Have a great day!", "Good night!"
        ]
        for i in range(20):
            sender = random.choice(users)
            recipient = random.choice([u for u in users if u != sender])
            message_text = random.choice(messages)
            Message.objects.create(
                sender=sender,
                recipient=recipient,
                text=message_text,
                timestamp=timezone.now()
            )
            self.stdout.write(
                f'Message from {sender.username} to '
                f'{recipient.username}: "{message_text}"')
