# Generated by Django 5.0.4 on 2024-04-10 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_schedule_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
