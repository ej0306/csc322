# Generated by Django 3.2.8 on 2021-12-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0025_auto_20211209_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='current_period',
            field=models.CharField(blank=True, choices=[('Class Set-Up Period', 'Class Set-Up Period'), ('Course Registration Period', 'Course Registration Period'), ('Class Running Period', 'Class Running Period'), ('Grading Period', 'Grading Period')], max_length=200, null=True),
        ),
    ]
