# Generated by Django 4.2 on 2023-05-10 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lending", "0003_alter_lending_devolution_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lending",
            name="devolution_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 13, 14, 57, 44, 935068, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
