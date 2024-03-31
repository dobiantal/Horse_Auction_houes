from django.db import models

class Policy(models.Model):
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    policy = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
