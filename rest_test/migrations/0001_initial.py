# Generated by Django 4.0.4 on 2022-05-07 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=40)),
                ('maker', models.CharField(max_length=60)),
                ('year', models.IntegerField()),
                ('vin', models.CharField(max_length=100)),
            ],
        ),
    ]
