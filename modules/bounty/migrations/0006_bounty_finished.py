# Generated by Django 2.0.8 on 2018-12-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0005_userbounty_reward_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
