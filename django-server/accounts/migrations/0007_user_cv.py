# Generated by Django 5.0 on 2024-01-05 01:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_usermessage"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="cv",
            field=models.TextField(null=True),
        ),
    ]