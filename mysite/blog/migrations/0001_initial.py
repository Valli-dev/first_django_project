# Generated by Django 3.2 on 2021-05-10 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('department', models.CharField(max_length=50)),
                ('date_of_resumption', models.DateField(default=datetime.datetime.today)),
            ],
        ),
    ]
