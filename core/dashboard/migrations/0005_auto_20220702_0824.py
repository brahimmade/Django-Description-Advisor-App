# Generated by Django 3.2.13 on 2022-07-02 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20220608_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='related_job_titles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='related_descriptions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jobtitle',
            name='related_skills',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='skill',
            name='related_job_titles',
            field=models.IntegerField(default=0),
        ),
    ]
