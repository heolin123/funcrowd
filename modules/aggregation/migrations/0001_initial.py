# Generated by Django 2.0.8 on 2019-03-03 23:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0014_item_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAggregation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(max_length=20)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aggregations', to='tasks.Item')),
            ],
            options={
                'verbose_name_plural': 'ItemAggregations',
            },
        ),
    ]
