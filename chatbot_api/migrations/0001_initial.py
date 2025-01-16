# Generated by Django 5.1.4 on 2025-01-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MessageExplainer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("_input", models.TextField()),
                ("_output", models.TextField()),
            ],
            options={
                "db_table": "message_explainer",
            },
        ),
    ]
