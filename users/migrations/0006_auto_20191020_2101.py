# Generated by Django 2.0.8 on 2019-10-20 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_endworker_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endworker',
            old_name='experience',
            new_name='exp',
        ),
    ]
