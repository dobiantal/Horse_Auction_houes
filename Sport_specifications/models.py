from django.db import models

class Sport_specification(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    sport_major = models.CharField(max_length=100, null=False)

    class Meta:
        ordering = ['id']