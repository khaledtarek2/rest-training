# Generated by Django 4.0.4 on 2022-05-16 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_test', '0003_alter_car_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='collection',
            field=models.ForeignKey(blank=True, db_constraint=None, on_delete=django.db.models.deletion.CASCADE, to='rest_test.collection'),
        ),
    ]