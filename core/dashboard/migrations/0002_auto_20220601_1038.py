# Generated by Django 3.2.13 on 2022-06-01 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobtitle',
            options={'ordering': ('-created_date',)},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('-created_date',)},
        ),
    ]
