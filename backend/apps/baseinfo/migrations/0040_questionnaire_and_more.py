# Generated by Django 4.1.5 on 2023-02-07 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0039_expertgroupaccess_invite_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_date', models.DateTimeField(auto_now=True)),
                ('index', models.PositiveIntegerField(null=True)),
                ('assessment_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaires', to='baseinfo.assessmentprofile')),
            ],
            options={
                'verbose_name': 'Questionnaire',
                'verbose_name_plural': 'Questionnaires',
            },
        ),
        migrations.RemoveField(
            model_name='assessmentsubject',
            name='metric_categories',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='metric_category',
        ),
        migrations.DeleteModel(
            name='MetricCategory',
        ),
        migrations.AddField(
            model_name='assessmentsubject',
            name='questionnaires',
            field=models.ManyToManyField(related_name='assessment_subjects', to='baseinfo.questionnaire'),
        ),
        migrations.AddField(
            model_name='metric',
            name='questionnaire',
            field=models.ForeignKey(default=66, on_delete=django.db.models.deletion.CASCADE, to='baseinfo.questionnaire'),
            preserve_default=False,
        ),
    ]
