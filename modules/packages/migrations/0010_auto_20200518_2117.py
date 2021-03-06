# Generated by Django 2.2.4 on 2020-05-18 21:17

from django.db import migrations, models
import modules.packages.models.utils


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0009_auto_20200513_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='missionpackages',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='missionpackages',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userpackageprogress',
            name='reward_token',
            field=models.CharField(default=modules.packages.models.utils.get_reward_token, max_length=32),
        ),
    ]
