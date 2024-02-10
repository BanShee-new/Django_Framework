from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    number_phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Client -> name: {self.name}, email: {self.email},' \
               f'number_phone: {self.number_phone}, address: {self.address}'


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product-> {self.product_name}, {self.description}, {self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order-> {self.client}, {self.products}, {self.total_price}'
