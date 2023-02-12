# Generated by Django 4.1.5 on 2023-02-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0043_remove_assessmentprofile_is_default_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionnaire',
            options={'verbose_name': 'Questionnaire', 'verbose_name_plural': 'Questionnaires'},
        ),
        migrations.AlterUniqueTogether(
            name='questionnaire',
            unique_together={('title', 'assessment_profile')},
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='index',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='questionnaire',
            unique_together={('index', 'assessment_profile'), ('title', 'assessment_profile')},
        ),
    ]
