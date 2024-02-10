from datetime import timedelta, datetime

from django.shortcuts import render
import logging
import random
from django.utils import timezone
from .models import Client, Product, Order

logger = logging.getLogger(__name__)


def index(request):
    """Список всех клиентов"""
    logger.debug('request index')
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'home_work_3/index.html', context)


def fake_clients(request, count):
    """ Generate fake clients (arg: count)"""
    for i in range(count):
        client = Client(name=f'Client #{i + 1}',
                        email=f'Client{i}@mail.com',
                        number_phone=f'+7({i})927654',
                        address=f'address #{i + 1}',
                        registration_date=timezone.now())
        client.save()

    context = {'content': f'Create {count} clients !'}
    logger.debug(f'request: fake_clients, Create {count} clients !')
    return render(request, 'home_work_3/fake.html', context)


def fake_products(request, count):
    """ Generate fake products (arg: count)"""
    for i in range(count):
        product = Product(product_name=f'product #{i+1}',
                          description=f'description #{i+1}',
                          price=random.randint(1, 100),
                          quantity=random.randint(10, 100),
                          date_ordered=timezone.now())
        product.save()

    context = {'content': f'Create {count} products !'}
    logger.debug(f'request: fake_products, Create {count} products !')
    return render(request, 'home_work_3/fake.html', context)


def fake_orders(request, pk, count):
    """ Generate fake orders (arg: pk(id client), count: count products)"""
    client = Client.objects.filter(pk=pk).first()
    order = Order(client=client, total_price=0, date_ordered=timezone.now())
    for i in range(count):
        product = Product.objects.filter(pk=(i+1)).first()
        print(product)

        order.total_price += product.price
        order.save()
        order.products.add(product)
    context = {'content': f'Create order: 1-{count} fake products, for client(pk={pk}) ! < {client}'}
    logger.debug(f'Create order: 1-{count} fake products, for client(pk={pk}) !')
    return render(request, 'home_work_3/fake.html', context)
    # удалить
    # client = Client.objects.filter(pk=pk).first()
    # product = Product.objects.filter(pk=11).first()
    # product_2 = Product.objects.filter(pk=10).first()
    # order = Order(client=client, total_price=0, date_ordered=timezone.now())
    # order.total_price += product.price
    # order.total_price += product_2.price
    # order.save()
    # order.products.add(product, product_2)


def show_client_orders_test(request, pk):
    """(тест)Вывод всех заказов клиента"""
    client = Client.objects.filter(pk=pk).first()
    context = {'content': f'< {client}'}
    orders = Order.objects.filter(client=client).all()

    print('всего у клиента: ', len(orders), 'заказ(ов)')
    print('общее инфо: ', orders[0])
    print('Клиент имя: ', orders[0].client.name)
    # print(type(orders[0].products))

    print(orders[0].products.values()[0]['product_name'])

    print('Список товаров в заказе:')
    for i in orders[0].products.values():
        print(i['product_name'])
    # print(orders[0].total_price)
    # print(orders[0].date_ordered)
    return render(request, 'home_work_3/fake.html', context)


def show_client_orders(request, pk):
    """Вывод всех заказов клиента"""
    client = Client.objects.filter(pk=pk).first()
    orders = Order.objects.filter(client=client).all()

    context = {
        'name': client.name,
        'count': len(orders),
        'orders': orders,
    }
    return render(request, 'home_work_3/show_client_orders.html', context)


def list_goods_period_of_time(request, days, pk):
    """Выводит список добавленных клиентом товаров из всех его заказов"""
    today = datetime.now()
    range_days = today - timedelta(days=days)
    client = Client.objects.filter(pk=pk).first()
    orders = Order.objects.filter(client=client, date_ordered__range=(range_days, today)).all()
    context = {
        'days': days,
        'range_days': range_days,
        'name': client.name,
        'orders': orders,
        'count': len(orders),
    }
    return render(request, 'home_work_3/list_goods_period_of_time.html', context)
