# Generated by Django 3.1.6 on 2021-02-25 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210220_1957'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.AddField(
            model_name='player',
            name='team_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]