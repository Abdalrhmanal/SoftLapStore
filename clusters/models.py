from django.db import models

# Create your models here.
class Cluster(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CustomerSimilarity(models.Model):
    id = models.AutoField(primary_key=True)
    user1_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user1')
    user2_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user2')
    similarity = models.FloatField()