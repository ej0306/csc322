# Generated by Django 3.2.8 on 2021-12-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduation', '0004_auto_20211207_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduatingclass',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]