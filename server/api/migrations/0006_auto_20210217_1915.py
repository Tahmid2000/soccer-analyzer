# Generated by Django 3.1.6 on 2021-02-18 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210217_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='successfull_duels',
            new_name='successful_duels',
        ),
    ]