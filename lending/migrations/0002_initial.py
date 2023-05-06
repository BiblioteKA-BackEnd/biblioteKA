# Generated by Django 4.2 on 2023-05-06 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lending", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lending",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="user_lending",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
