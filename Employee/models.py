from django.db import models
from Policy.models import Policy
class Employee(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    Fname = models.CharField(max_length=100, null=False)
    Lname = models.CharField(max_length=100, null=False)
    account_name = models.CharField(max_length=100, null=False, unique=True)
    email = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=100, null=False)
    policy_id = models.ForeignKey(Policy,on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(null=False, auto_created=True)
    updated_at = models.DateTimeField(null=False, auto_created=True)
    deleted_at = models.DateTimeField(null=True)
    extra_kwargs = {
        'password': {'write_only':True}
    }

    class Meta:
        ordering = ['id']

