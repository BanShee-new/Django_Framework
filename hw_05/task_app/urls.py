from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_product/', views.add_product, name='add_product'),
    path('show_products/', views.show_products, name='show_products'),
    path('update_product/', views.update_product, name='update_product'),
    path('show_clients/', views.show_clients, name='show_clients'),
]
