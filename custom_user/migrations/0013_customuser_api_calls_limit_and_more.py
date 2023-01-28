# Generated by Django 4.1.5 on 2023-01-28 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("custom_user", "0012_tempusers_auth_token_tempusers_verified_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="api_calls_limit",
            field=models.IntegerField(blank=True, default=50, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="access_allowed",
            field=models.BooleanField(default=True),
        ),
    ]
