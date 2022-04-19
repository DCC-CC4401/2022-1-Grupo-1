# Generated by Django 3.2.12 on 2022-04-19 05:45

from django.db import migrations

def create_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.bulk_create(
        [
            Group(name="resident"),
            Group(name="doorman"),
        ]
    )

def revert_migration(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(
        name__in=[
            "resident",
            "doorman",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220417_1942'),
    ]

    operations = [
        migrations.RunPython(create_groups, revert_migration),
    ]