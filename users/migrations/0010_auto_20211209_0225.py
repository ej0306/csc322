# Generated by Django 3.2.8 on 2021-12-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_merge_20211208_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='special_registration',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='suspend_next_sem',
            field=models.BooleanField(default=False),
        ),
    ]
