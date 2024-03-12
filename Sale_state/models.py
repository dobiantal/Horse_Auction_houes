from django.db import models

class Sale_state(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    state = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
