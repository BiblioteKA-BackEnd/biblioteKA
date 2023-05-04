# Generated by Django 4.2 on 2023-05-04 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="copy",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="copies",
                to="books.book",
            ),
        ),
        migrations.AlterField(
            model_name="copy",
            name="is_available",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
