# Generated by Django 3.2.8 on 2021-11-12 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211112_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gpa',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='graduation_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='sc_state',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=''),
        ),
    ]
