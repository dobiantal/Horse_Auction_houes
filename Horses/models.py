from django.db import models

import Sport_specifications
from Beeders.models import Beeders
from Bidder.models import Bidder
from Sale_state.models import Sale_state


class Horse(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    horse_name = models.CharField(max_length=100, null=False)
    horse_gender = models.CharField(max_length=100, null=False)
    horse_was_born = models.DateTimeField(null=False)
    horse_weight = models.IntegerField(null=False)
    horse_height_at_withers = models.FloatField(null=False)
    start_price = models.IntegerField(null=False)
    bid_step = models.IntegerField(null=False)
    horse_highest_sport_result = models.CharField(max_length=255)
    actual_price = models.IntegerField(null=False)
    bid_start = models.DateTimeField(null=False)
    breeder_id = models.ForeignKey(Beeders,on_delete=models.CASCADE)
    sport_specification_id = models.ForeignKey(Sport_specifications,on_delete=models.CASCADE)
    sale_state_id = models.ForeignKey(Sale_state,on_delete=models.CASCADE)
    bidder_id = models.ForeignKey(Bidder,on_delete=models.CASCADE)


    class Meta:
        ordering = ['id']
