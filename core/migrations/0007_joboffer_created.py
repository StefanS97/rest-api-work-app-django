# Generated by Django 3.1.5 on 2021-03-20 23:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_joboffer_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]