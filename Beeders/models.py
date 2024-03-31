from django.db import models

class Beeders(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    Beeder_F_name = models.CharField(max_length=100, null=False)
    Beeder_L_name = models.CharField(max_length=100, null=False)
    Stable_name = models.CharField(max_length=100, null=False)
    Beeder_phone = models.CharField(max_length=100, null=False)
    Beeder_email = models.CharField(max_length=100, null=False)
    Beeder_webpage = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ['id']