# Generated by Django 3.1.6 on 2021-02-27 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210225_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamh2hfixtures',
            name='date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]