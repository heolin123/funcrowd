# Generated by Django 2.0.8 on 2019-02-12 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermissionstats',
            old_name='items_done',
            new_name='agreement_ranking_position',
        ),
        migrations.RenameField(
            model_name='userstats',
            old_name='items_done',
            new_name='agreement_ranking_position',
        ),
        migrations.AddField(
            model_name='usermissionstats',
            name='agreement_ranking_percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='usermissionstats',
            name='high_agreement_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstats',
            name='agreement_ranking_percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='userstats',
            name='high_agreement_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='missionstats',
            name='mission',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Mission'),
        ),
        migrations.AlterField(
            model_name='usermissionstats',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='local_mission_stats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userstats',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='local_stats', to=settings.AUTH_USER_MODEL),
        ),
    ]
