# Generated by Django 4.2 on 2023-05-04 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("follows", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="follow",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="user_follows",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]