# Generated by Django 2.2.4 on 2020-01-30 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0037_auto_20191208_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='initial_status',
            field=models.CharField(blank=True, choices=[('HIDDEN', 'Hidden'), ('LOCKED', 'Locked'), ('UNLOCKED', 'Unlocked'), ('IN_PROGRESS', 'InProgress'), ('FINISHED', 'Finished')], max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='usermissionprogress',
            name='status',
            field=models.CharField(choices=[('HIDDEN', 'Hidden'), ('LOCKED', 'Locked'), ('UNLOCKED', 'Unlocked'), ('IN_PROGRESS', 'InProgress'), ('FINISHED', 'Finished')], max_length=32),
        ),
    ]
