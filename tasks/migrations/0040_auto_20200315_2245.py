# Generated by Django 2.2.4 on 2020-03-15 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0039_auto_20200211_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='initial_status',
            field=models.CharField(blank=True, choices=[('LOCKED', 'Locked'), ('UNLOCKED', 'Unlocked'), ('IN_PROGRESS', 'InProgress'), ('FINISHED', 'Finished'), ('PERMANENT', 'Permanent')], max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='usertaskprogress',
            name='status',
            field=models.CharField(choices=[('LOCKED', 'Locked'), ('UNLOCKED', 'Unlocked'), ('IN_PROGRESS', 'InProgress'), ('FINISHED', 'Finished'), ('PERMANENT', 'Permanent')], default='LOCKED', max_length=32),
        ),
    ]
