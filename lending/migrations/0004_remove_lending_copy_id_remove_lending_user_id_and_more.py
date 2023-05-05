# Generated by Django 4.2 on 2023-05-05 12:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0003_copy_lent_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lending", "0003_alter_lending_devolution_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lending",
            name="copy_id",
        ),
        migrations.RemoveField(
            model_name="lending",
            name="user_id",
        ),
        migrations.AddField(
            model_name="lending",
            name="copy",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="copy_lending",
                to="books.copy",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="lending",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="user_lending",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="lending",
            name="devolution_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 7, 12, 54, 44, 459658, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
