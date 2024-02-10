from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('request: index')
    return HttpResponse('<h2>Task 2(seminar3), работаем через консоль, загляните в файл view</h2>')


# Добавить продукты:
# python .\manage.py fake_product 50(количество фейковых продуктов)

# Добавить клиентов и заказы:
# python .\manage.py fake_client_order 5

# отработал команды из лекции, применил их к данной задаче
# команды по пути.\management\commands
