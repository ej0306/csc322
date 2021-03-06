# Generated by Django 3.2.8 on 2021-12-09 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0024_merge_20211209_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='current_period',
            field=models.CharField(blank=True, choices=[('Class Set-Up Period', 'Class Set-Up Period'), ('Course Registration Period', 'Course Registration Period'), ('Class Running Period', 'Class Running Period'), ('Grading Period', 'Grading Period')], default='', max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='AutomaticWarning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warning_text', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
