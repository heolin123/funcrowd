# Generated by Django 2.2 on 2019-11-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0012_auto_20191111_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='autoreject',
            field=models.BooleanField(default=False),
        ),
    ]
