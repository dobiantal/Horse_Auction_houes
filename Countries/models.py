from django.db import models

class Countries(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    Country = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ['id']
