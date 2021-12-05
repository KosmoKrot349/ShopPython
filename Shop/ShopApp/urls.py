from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from . import  views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index, name='home'),
    path('admin', views.Index, name='admin'),
    path('buy/<int:ProductId>', views.Buy, name='buy'),
    path('myOrders', views.MyOrders, name='myOrders')
]

