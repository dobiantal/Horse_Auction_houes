from django.db import models
from django.contrib.auth.models import AbstractUser
class Employee(AbstractUser):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    Fname = models.CharField(max_length=100, null=False)
    Lname = models.CharField(max_length=100, null=False)
    account_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=100, null=False)
    Policy = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=False)
    deleted_at = models.DateTimeField(null=False)

    class Meta:
        ordering = ['id']