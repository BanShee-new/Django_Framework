from django.core.management.base import BaseCommand
from task.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(
            name=f'Kate',
            email=f'beckinsale@mail.ru',
            number_phone=f'+(0)92707585',
            address=f'New York'
        )
        client.save()
        self.stdout.write(f'{client}')
