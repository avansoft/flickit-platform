# Generated by Django 4.1.5 on 2023-01-30 10:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baseinfo', '0035_alter_assessmentprofile_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expertgroup',
            name='users',
        ),
        migrations.AddField(
            model_name='expertgroup',
            name='users',
            field=models.ManyToManyField(related_name='expert_groups', through='baseinfo.ExpertGroupAccess', to=settings.AUTH_USER_MODEL),
        ),
    ]
