# Generated by Django 5.0.10 on 2025-01-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_user_date_password_last_updated"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="date_api_key_last_used",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Date api key used"
            ),
        ),
    ]
