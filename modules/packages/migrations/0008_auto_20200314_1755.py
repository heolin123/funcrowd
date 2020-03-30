# Generated by Django 2.2.4 on 2020-03-14 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0007_userpackageprogress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missionpackages',
            name='multiple_annotations',
        ),
        migrations.AlterField(
            model_name='userpackageprogress',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='packages.Package'),
        ),
    ]