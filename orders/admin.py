from django.contrib import admin

from orders.models import Order
from orders.models import OrderDetail
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderDetail)