# Generated by Django 2.0.8 on 2019-02-27 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0006_remove_usermissionstats_high_agreement_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstats',
            name='high_agreement_count',
        ),
    ]
