# Generated by Django 4.0.4 on 2022-05-14 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_test', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='year',
            new_name='release_year',
        ),
    ]
