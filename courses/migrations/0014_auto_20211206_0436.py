# Generated by Django 3.2.8 on 2021-12-06 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_waitlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='days',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='classes',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='classes',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
