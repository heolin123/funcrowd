# Generated by Django 2.0.8 on 2018-12-16 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_task_instruction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annotation',
            old_name='is_skipped',
            new_name='skipped',
        ),
    ]
