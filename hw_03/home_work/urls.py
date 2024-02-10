from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fake_clients/<int:count>/', views.fake_clients, name='fake_clients'),
    path('fake_products/<int:count>/', views.fake_products, name='fake_products'),
    path('fake_orders/<int:pk>/<int:count>/', views.fake_orders, name='fake_orders'),
    path('show_client_orders/<int:pk>/', views.show_client_orders, name='show_client_orders'),
    path('list_goods_period_of_time/<int:days>/<int:pk>',
         views.list_goods_period_of_time, name='list_goods_period_of_time'),
]
