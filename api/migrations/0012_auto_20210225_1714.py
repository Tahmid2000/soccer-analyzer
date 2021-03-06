# Generated by Django 3.1.6 on 2021-02-25 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_searchteam_team_teamh2hfixtures_teamh2hstats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='clicks',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='country',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='founded',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='image_path',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='venue_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
