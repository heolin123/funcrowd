# Generated by Django 2.0.8 on 2018-10-21 23:26

from django.db import migrations, models
import django.db.models.deletion
import sortedm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('items', sortedm2m.fields.SortedManyToManyField(help_text=None, to='tasks.Item')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='missions', to='tasks.Mission')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
