# Generated by Django 5.0.2 on 2024-03-16 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cities', '0001_initial'),
        ('Countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Phone_number', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('City_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cities.cities')),
                ('Country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Countries.countries')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
