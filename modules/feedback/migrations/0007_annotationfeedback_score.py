# Generated by Django 2.0.8 on 2019-02-27 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_auto_20181201_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationfeedback',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
