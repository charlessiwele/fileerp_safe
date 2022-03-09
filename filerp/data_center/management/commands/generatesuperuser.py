import logging
import pathlib
import random
import string

from django.contrib.auth.models import User
from django.core.management import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'GENERATE A SUPERUSER'
    """
    This command is useful for generating a superuser with randomly generated username and email detail combo
    The details will be written to a file including the default password
    """

    def handle(self, *args, **options):
        try:
            pathlib.Path('./superusers/').mkdir(parents=True, exist_ok=True)
            print('Welcome to custom superuser generator')
            username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            user_email = f'{username}@{username[:4]}.{username[:2]}'
            password = username[:5]
            result = User.objects.create_superuser(username, user_email, password)
            print(f'username: {username} user_email: {user_email}, password: {password}')
            with (open(f'./superusers/{username}.txt', 'w+')) as writer:
                writer.write(f'username: {username}')
                writer.write(f'\npassword: {password}')
                writer.write(f'\nuser_email: {user_email}')
        except Exception as exception:
            print(exception.__str__())
