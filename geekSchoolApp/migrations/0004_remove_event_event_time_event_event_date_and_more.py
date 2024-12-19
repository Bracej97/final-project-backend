# Generated by Django 4.2.17 on 2024-12-19 07:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('geekSchoolApp', '0003_remove_event_created_user_remove_event_end_datetime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_time',
        ),
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_end',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='event_start',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faq',
            name='category',
            field=models.CharField(default='Test', max_length=500),
            preserve_default=False,
        ),
    ]
