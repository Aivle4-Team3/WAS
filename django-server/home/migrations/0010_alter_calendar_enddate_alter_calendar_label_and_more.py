# Generated by Django 5.0 on 2024-01-04 05:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0009_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calendar",
            name="enddate",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="calendar",
            name="label",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="calendar",
            name="startdate",
            field=models.DateTimeField(),
        ),
    ]
