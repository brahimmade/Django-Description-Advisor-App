# Generated by Django 3.2.13 on 2022-08-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20220702_0824'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_core', models.BooleanField(default=False)),
                ('text', models.TextField()),
                ('is_archived', models.BooleanField(default=False)),
                ('is_marked', models.BooleanField(default=False)),
                ('related_job_titles', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('job_title', models.ManyToManyField(to='dashboard.JobTitle')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]
