# Generated by Django 2.2.4 on 2020-03-02 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0009_missionsdoneachievement_tasksdoneachievement'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='auto_close',
            field=models.BooleanField(default=False),
        ),
    ]
