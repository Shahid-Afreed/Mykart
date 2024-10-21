
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('product_list',views.list_products,name='product_list'),
    path('product_details/<pk>',views.detail_products,name='product_details'),
]
