from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    country_id = models.ForeignKey('countries.Country', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    logo = models.TextField(null=True, blank=True)
    date_of_establishment = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name