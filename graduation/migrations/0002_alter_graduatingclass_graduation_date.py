# Generated by Django 3.2.8 on 2021-12-07 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduatingclass',
            name='graduation_date',
            field=models.DateTimeField(),
        ),
    ]
