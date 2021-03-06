# Generated by Django 3.2.8 on 2021-12-07 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_reports_options'),
        ('courses', '0015_remove_classes_days_and_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarningCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
    ]
