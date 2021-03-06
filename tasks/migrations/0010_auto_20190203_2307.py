# Generated by Django 2.0.8 on 2019-02-03 23:07

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20181216_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('IN_PROGRESS', 'IN_PROGRESS'), ('VERIFICATION', 'VERIFICATION'), ('CLOSED', 'CLOSED')], default='NEW', max_length=20)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField()),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='tasks.Mission')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='tasks.Document'),
        ),
    ]
