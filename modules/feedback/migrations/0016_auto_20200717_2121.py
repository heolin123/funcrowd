# Generated by Django 2.2.4 on 2020-07-17 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0015_annotationfeedback_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='type',
            field=models.CharField(choices=[('NONE', 'None'), ('CONFIRM_ONLY', 'Confirm only'), ('BINARY', 'Binary'), ('QUIZ', 'Quiz'), ('QUESTIONNAIRE', 'Questionnaire'), ('POINTS', 'Points'), ('NER', 'NER'), ('CLASSIFICATION', 'Classification'), ('REGRESSION', 'Regression')], default='NONE', max_length=32),
        ),
    ]
