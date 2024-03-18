# Generated by Django 5.0.2 on 2024-03-18 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
        ('Policy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='employee',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Policy',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='username',
        ),
        migrations.AddField(
            model_name='employee',
            name='policy_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Policy.policy'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='account_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
