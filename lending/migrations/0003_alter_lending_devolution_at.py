# Generated by Django 4.2 on 2023-05-05 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lending", "0002_alter_lending_devolution_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lending",
            name="devolution_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 12, 30, 21, 694493, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
