# Generated by Django 4.1.5 on 2023-02-09 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baseinfo', '0041_alter_questionnaire_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertgroup',
            name='about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='expertgroup',
            name='bio',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='expertgroup',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
