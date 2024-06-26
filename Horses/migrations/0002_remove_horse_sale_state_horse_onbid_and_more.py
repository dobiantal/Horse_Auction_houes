# Generated by Django 5.0.2 on 2024-03-24 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Beeders', '0001_initial'),
        ('Bidder', '0002_alter_bidder_password_alter_bidder_username'),
        ('Horses', '0001_initial'),
        ('Sale_state', '0001_initial'),
        ('Sport_specifications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horse',
            name='sale_state',
        ),
        migrations.AddField(
            model_name='horse',
            name='onbid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='horse',
            name='sale_state_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Sale_state.sale_state'),
        ),
        migrations.AlterField(
            model_name='horse',
            name='bidder_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bidder.bidder'),
        ),
        migrations.AlterField(
            model_name='horse',
            name='breeder_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Beeders.beeders'),
        ),
        migrations.AlterField(
            model_name='horse',
            name='sport_specification_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sport_specifications.sport_specification'),
        ),
    ]
