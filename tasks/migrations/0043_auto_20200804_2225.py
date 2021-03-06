# Generated by Django 2.2.4 on 2020-08-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0042_auto_20200622_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermissionprogress',
            name='bonus_exp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usermissionprogress',
            name='exp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itemtemplatefield',
            name='type',
            field=models.CharField(choices=[('int', 'int'), ('float', 'float'), ('str', 'str'), ('bool', 'bool'), ('list', 'list')], default='str', max_length=10),
        ),
    ]
