# Generated by Django 3.2.8 on 2021-12-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_alter_classes_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='days',
            field=models.CharField(choices=[('Mon', 'Mon'), ('Tue', 'Tue'), ('Wed', 'Wed'), ('Thu', 'Thu'), ('Fri', 'Fri'), ('Sat', 'Sat'), ('Sun', 'Sun'), ('Mon, Wed', 'Mon, Wed'), ('Tue, Thu', 'Tue, Thu'), ('Mon, Wed, Thu', 'Mon, Wed, Thu'), ('Tue, Thu, Fri', 'Tue, Thu, Fri'), ('Wed, Fri', 'Wed, Fri'), ('Sat, Sun', 'Sat, Sun')], max_length=50, null=True),
        ),
    ]
