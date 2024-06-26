from django.contrib import admin

from ratings.models import ProductRating

from ratings.models import ProductFavorite

# Register your models here.
admin.site.register(ProductRating)
admin.site.register(ProductFavorite)
