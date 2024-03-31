# Generated by Django 5.0.2 on 2024-03-24 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Policy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Fname', models.CharField(max_length=100)),
                ('Lname', models.CharField(max_length=100)),
                ('account_name', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=100)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('policy_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Policy.policy')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]