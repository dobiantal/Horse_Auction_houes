from django.db import models

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
    breeder_id = models.BigIntegerField(null=False)
    sport_specification_id = models.BigIntegerField(null=False)
    sale_state = models.BigIntegerField(null=False)
    bidder_id = models.BigIntegerField(null=False)


    class Meta:
        ordering = ['id']
