from django.db import models
from Countries.models import Countries
from Cities.models import Cities

class Bidder(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    Username = models.CharField(max_length=255, null=False, unique=True)
    Password = models.CharField(max_length=255, null=False)
    First_name = models.CharField(max_length=100, null=False)
    Last_name = models.CharField(max_length=100, null=False)
    Country_id = models.ForeignKey(Countries,on_delete=models.CASCADE)
    Phone_number = models.CharField(max_length=100, null=False)
    Email = models.CharField(max_length=100, null=False)
    Address = models.IntegerField
    City_id = models.ForeignKey(Cities,on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']