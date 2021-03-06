# Generated by Django 2.0.8 on 2018-12-09 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0007_auto_20181209_1559'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bounty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('OPEN', 'OPEN'), ('FINISHED', 'FINISHED'), ('CLOSED', 'CLOSED')], default='NEW', max_length=10)),
                ('annotations_initial', models.IntegerField(default=0)),
                ('annotations_done', models.IntegerField(default=0)),
                ('annotations_target', models.IntegerField(default=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bounties', to='tasks.Task')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
