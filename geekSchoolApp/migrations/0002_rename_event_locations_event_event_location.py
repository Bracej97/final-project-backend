# Generated by Django 4.2.17 on 2024-12-12 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geekSchoolApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_locations',
            new_name='event_location',
        ),
    ]
