from django.core.management.base import BaseCommand
from task.models import Client, Order, Product


class Command(BaseCommand):
    help = "Generate fake Client and Order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(
                name=f'Name #{i}',
                email=f'mail{i}@mail.ru',
                number_phone=f'+({i})92707585',
                address=f'address #{i}'
            )
            client.save()
            order = Order(client=client)
            total_price = 0
            for j in range(1, count + 1):
                product = Product.objects.filter(pk=i).first()
                total_price += float(product.price)
                order.total_price = total_price
                order.save()
                order.products.add(product)
        print(f'Success, {count} clients for {count} products')
