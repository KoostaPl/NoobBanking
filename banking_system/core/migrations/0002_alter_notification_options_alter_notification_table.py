# Generated by Django 5.0.7 on 2024-07-29 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notification",
            options={},
        ),
        migrations.AlterModelTable(
            name="notification",
            table="notifications",
        ),
    ]