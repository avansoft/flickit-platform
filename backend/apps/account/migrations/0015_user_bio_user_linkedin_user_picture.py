# Generated by Django 4.1.5 on 2023-02-22 07:43

import common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_space_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(null=True, upload_to='user/images', validators=[common.validators.validate_file_size]),
        ),
    ]
