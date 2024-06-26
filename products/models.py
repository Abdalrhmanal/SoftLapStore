from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    cluster_id = models.ForeignKey('clusters.Cluster', on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    company_id = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    category_id = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    face_image = models.TextField()
    price = models.FloatField()
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.TextField(null=True, blank=True)