from django.db import models

from django.db import models
from Horses.models import Horse

class Horse_images(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    image_path = models.ImageField(upload_to='images/',null=False)
    horse_id = models.ForeignKey(Horse,on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
