import decimal

from django.contrib import admin
from . import models


@admin.action(description='Увеличить цену товара на 15 процентов')
def change_price(modeladmin, request, queryset):
    """Добавление действий"""
    old_price = queryset.values()[0]['price']
    queryset.update(price=old_price * decimal.Decimal('1.15'))


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'quantity', 'date_ordered']
    ordering = ['-date_ordered']
    list_filter = ['date_ordered', 'price', 'quantity']
    search_fields = ['product_name']
    search_help_text = 'Поиск по названию продукта'
    actions = [change_price]

    fields = ['product_name', 'description', 'price', 'quantity', 'date_ordered', 'product_image']
    readonly_fields = ['product_image', 'date_ordered']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'number_phone']
    ordering = ['name']
    list_filter = ['registration_date']
    search_fields = ['name']
    search_help_text = 'Поиск по имени клиента'
    readonly_fields = ['registration_date', 'name']

    # Детальная настройка отображения полей
    fieldsets = [
        (
            'Имя клиента',
            {
                'classes': ['wide'],
                'fields': ['name'],
                # Первая группа будет содержать только поле "name", она будет иметь
                # класс "wide", что означает, что она будет занимать все доступное место
                # на странице.
            },
        ),
        (
            'Редактировать данные клиента',
            {
                'classes': ['collapse'],
                'description': 'Будьте внимательны при редактировании данных!',
                'fields': ['email', 'number_phone', 'address'],
                # Вторая группа будет содержать поля 'email', 'number_phone', 'address', они
                # будут скрыты по умолчанию (класс "collapse"), но можно будет
                # развернуть и отредактировать эту группу, нажав на соответствующий заголовок. Под
                # заголовком отобразится описание группы registration_date
            },
        ),
        (
            'Дата регистрации клиента',
            {
                'classes': ['wide'],
                'fields': ['registration_date'],
            },
        )
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'date_ordered', 'total_price']
    ordering = ['date_ordered']
    list_filter = ['date_ordered']
    search_fields = ['date_ordered']
    search_help_text = 'Поиск по дате'
    readonly_fields = ['client', 'products', 'date_ordered', 'total_price']
    fieldsets = [
        (
            'Клиент',
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Что купил',
            {
                'classes': ['wide'],
                'fields': ['products'],
            },
        ),
        (
            'Дата оформления заказа',
            {
                'classes': ['wide'],
                'fields': ['date_ordered'],
            },
        ),
        (
            'Итоговая цена заказа',
            {
                'classes': ['wide'],
                'fields': ['total_price'],
            },
        )
    ]


admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
