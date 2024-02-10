from django.core.management.base import BaseCommand
from task.models import Client


class Command(BaseCommand):
    help = "Update client number_phone by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='client ID')
        parser.add_argument('phone', type=str, help='client phone')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        phone = kwargs.get('phone')
        client = Client.objects.filter(pk=pk).first()
        client.number_phone = phone
        client.save()
        self.stdout.write(f'{client}')
