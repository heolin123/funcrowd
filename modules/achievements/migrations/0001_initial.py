# Generated by Django 2.0.8 on 2019-09-26 23:24

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0026_auto_20190824_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={})),
                ('target', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': 'Achievements',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='UserAchievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='NEW', max_length=20)),
                ('value', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ItemDoneAchievement',
            fields=[
                ('achievement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='achievements.Achievement')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('achievements.achievement',),
        ),
        migrations.CreateModel(
            name='LoginCountAchievement',
            fields=[
                ('achievement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='achievements.Achievement')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('achievements.achievement',),
        ),
        migrations.CreateModel(
            name='ProgressAchievement',
            fields=[
                ('achievement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='achievements.Achievement')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('achievements.achievement',),
        ),
        migrations.AddField(
            model_name='userachievement',
            name='achievement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievements.Achievement'),
        ),
        migrations.AddField(
            model_name='userachievement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='achievement',
            name='mission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Mission'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_achievements.achievement_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
        ),
    ]
