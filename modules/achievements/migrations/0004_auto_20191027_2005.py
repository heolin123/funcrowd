# Generated by Django 2.0.8 on 2019-10-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0003_achievement_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievement',
            name='updated',
        ),
        migrations.AddField(
            model_name='userachievement',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
