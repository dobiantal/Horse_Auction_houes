# Generated by Django 5.0.2 on 2024-03-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beeders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Beeder_F_name', models.CharField(max_length=100)),
                ('Beeder_L_name', models.CharField(max_length=100)),
                ('Stable_name', models.CharField(max_length=100)),
                ('Beeder_phone', models.CharField(max_length=100)),
                ('Beeder_email', models.CharField(max_length=100)),
                ('Beeder_webpage', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
