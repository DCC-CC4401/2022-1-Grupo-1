# Generated by Django 3.2.12 on 2022-04-20 23:56

from django.db import migrations

def create_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.bulk_create(
        [
            Group(name="habitant"),
            Group(name="doorman"),
        ]
    )

def revert_migration(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(
        name__in=[
            "habitant",
            "doorman",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220420_2349'),
    ]

    operations = [
        migrations.RunPython(create_groups, revert_migration),
    ]
