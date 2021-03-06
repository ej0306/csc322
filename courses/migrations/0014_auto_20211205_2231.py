# Generated by Django 3.2.8 on 2021-12-06 03:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20211205_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='class_running_period_end',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='session',
            name='class_running_period_start',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='session',
            name='class_set_up_period_end',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='session',
            name='class_set_up_period_start',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='session',
            name='course_registration_period_end',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='session',
            name='course_registration_period_start',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='session',
            name='grading_period_end',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='session',
            name='grading_period_start',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
    ]
