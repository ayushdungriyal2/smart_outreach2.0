# Generated by Django 4.1.5 on 2023-01-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "custom_user",
            "0002_rename_celery_task_id_list_customuser_celery_task_id_add_domain_list_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="smart_lead_api_key",
            field=models.CharField(blank=True, default="", max_length=250, null=True),
        ),
    ]
