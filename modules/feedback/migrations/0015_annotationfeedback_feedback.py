# Generated by Django 2.2.4 on 2020-06-08 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0014_auto_20200209_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationfeedback',
            name='feedback',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.Feedback'),
        ),
    ]
