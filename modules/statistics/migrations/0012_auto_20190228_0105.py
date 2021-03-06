# Generated by Django 2.0.8 on 2019-02-28 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0011_auto_20190228_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermissionstats',
            old_name='_annotated_documents',
            new_name='annotated_documents',
        ),
        migrations.RenameField(
            model_name='usermissionstats',
            old_name='_annotated_items',
            new_name='annotated_items',
        ),
        migrations.RenameField(
            model_name='usermissionstats',
            old_name='_high_agreement_count',
            new_name='high_agreement_count',
        ),
        migrations.RenameField(
            model_name='userstats',
            old_name='_annotated_documents',
            new_name='annotated_documents',
        ),
        migrations.RenameField(
            model_name='userstats',
            old_name='_annotated_items',
            new_name='annotated_items',
        ),
        migrations.RenameField(
            model_name='userstats',
            old_name='_high_agreement_count',
            new_name='annotated_missions',
        ),
        migrations.AddField(
            model_name='usermissionstats',
            name='high_agreement_percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='userstats',
            name='high_agreement_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userstats',
            name='high_agreement_percentage',
            field=models.FloatField(default=0),
        ),
    ]
