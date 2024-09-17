# Generated by Django 5.1 on 2024-08-20 13:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunSQL(
            sql=[
                (
                    """
                CREATE TABLE IF NOT EXISTS posts (
                    "id" uuid PRIMARY KEY DEFAULT gen_random_uuid(),
                    "title" varchar,
                    "content" text
                );
                """
                )
            ],
            reverse_sql=[
                (
                    """
                DROP TABLE IF EXISTS posts;
                """
                )
            ],
        )
    ]
