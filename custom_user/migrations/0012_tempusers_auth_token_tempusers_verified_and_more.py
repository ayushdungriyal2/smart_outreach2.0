# Generated by Django 4.1.5 on 2023-01-25 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("custom_user", "0011_tempusers"),
    ]

    operations = [
        migrations.AddField(
            model_name="tempusers",
            name="auth_token",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="tempusers",
            name="verified",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]