# Generated by Django 2.0.8 on 2019-08-12 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0021_auto_20190723_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtemplatefield',
            name='default_value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tasks.ItemTemplateField'),
        ),
        migrations.AlterField(
            model_name='itemtemplatefield',
            name='data_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tasks.ItemTemplateField'),
        ),
    ]