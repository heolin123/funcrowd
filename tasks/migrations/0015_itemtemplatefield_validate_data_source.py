# Generated by Django 2.0.8 on 2019-03-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_item_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtemplatefield',
            name='validate_data_source',
            field=models.BooleanField(default=True),
        ),
    ]
