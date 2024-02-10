from django.core.management.base import BaseCommand
from task.models import Client


class Command(BaseCommand):
    help = "Get client by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='client ID')

    def handle(self, *args, **kwargs):
        id_ = kwargs['id']
        client = Client.objects.get(id=id_)
        self.stdout.write(f'{client}')
