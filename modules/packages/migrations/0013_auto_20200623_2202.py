# Generated by Django 2.2.4 on 2020-06-23 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0012_package_instruction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='instruction',
        ),
        migrations.AddField(
            model_name='missionpackages',
            name='instruction',
            field=models.TextField(blank=True, default=''),
        ),
    ]
