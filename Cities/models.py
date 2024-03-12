from django.db import models

class Cities(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    city_name = models.CharField(max_length=100, null=False)
    zip_code = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ['id']
