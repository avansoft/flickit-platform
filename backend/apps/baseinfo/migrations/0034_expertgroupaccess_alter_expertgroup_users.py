# Generated by Django 4.1.5 on 2023-01-28 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baseinfo', '0033_remove_assessmentprofile_likes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertGroupAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expert_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseinfo.expertgroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        # migrations.AlterField(
        #     model_name='expertgroup',
        #     name='users',
        #     field=models.ManyToManyField(related_name='expert_groups', through='baseinfo.ExpertGroupAccess', to=settings.AUTH_USER_MODEL),
        # ),
    ]
