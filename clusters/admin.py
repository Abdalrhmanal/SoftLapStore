from django.contrib import admin

from clusters.models import Cluster
from clusters.models import CustomerSimilarity
# Register your models here.
admin.site.register(Cluster)
admin.site.register(CustomerSimilarity)
