# Generated by Django 4.1.5 on 2023-01-19 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("custom_user", "0008_alter_customuser_client_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="client_id",
            field=models.CharField(
                default="1000.Z80WKB696P26IQF9OJ8N02WR37N0VY", max_length=250
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="client_secret",
            field=models.CharField(
                default="99191de808405a2f9bea51e79525fc0e1a3c7e73b9", max_length=250
            ),
        ),
    ]
