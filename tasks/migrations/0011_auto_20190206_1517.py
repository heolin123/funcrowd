# Generated by Django 2.0.8 on 2019-02-06 15:17

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20190203_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
