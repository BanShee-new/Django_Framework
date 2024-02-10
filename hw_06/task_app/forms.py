import datetime
from django import forms
from . import models


class ProductForm(forms.Form):
    product_name = forms.CharField(label='Название', max_length=30)
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.FloatField(label='Цена')
    quantity = forms.IntegerField(label='Остаток на складе')
    date_ordered = forms.DateField(label='Дата(по умолчанию сегодня)', initial=datetime.date.today,
                                   widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    product_image = forms.ImageField(label='Фото продукта(если есть)', required=False)


class ProductUpdateForm(forms.Form):
    product_update = forms.ModelChoiceField(label='Выберете продукт для редактирования',
                                            queryset=models.Product.objects.all(), empty_label='выберете продукт')
    product_name = forms.CharField(label='Название', max_length=30)
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.FloatField(label='Цена')
    quantity = forms.IntegerField(label='Остаток на складе')
    date_ordered = forms.DateField(label='Дата(по умолчанию сегодня)', initial=datetime.date.today,
                                   widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    product_image = forms.ImageField(label='Фото продукта(если есть)', required=False)
