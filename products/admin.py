from django.contrib import admin

from products.models import Product
from products.models import ProductImage
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)