from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    country_id = models.ForeignKey('countries.Country', on_delete=models.CASCADE)
    cluster_id = models.ForeignKey('clusters.Cluster', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile = models.TextField(null=True, blank=True)
    user_type = models.CharField(max_length=20, choices=(('admin', 'Admin'), ('customer', 'Customer')))

    def __str__(self):
        return self.name