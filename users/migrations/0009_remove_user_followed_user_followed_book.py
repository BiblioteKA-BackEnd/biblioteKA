# Generated by Django 4.2 on 2023-05-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("follows", "0002_alter_follow_user"),
        ("books", "0003_copy_lent_user"),
        ("users", "0008_alter_user_updated_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="followed",
        ),
        migrations.AddField(
            model_name="user",
            name="followed_book",
            field=models.ManyToManyField(
                related_name="followed_user", through="follows.Follow", to="books.book"
            ),
        ),
    ]
