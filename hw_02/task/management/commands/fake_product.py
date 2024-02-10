from django.core.management.base import BaseCommand
from task.models import Product


class Command(BaseCommand):
    help = "Generate fake product."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='n-fake product')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(
                product_name=f'product #{i}',
                description=f'description #{i}',
                price=i+55.99,
                quantity=i+10,
            )
            product.save()
        print(f'Success, {count} entries')
