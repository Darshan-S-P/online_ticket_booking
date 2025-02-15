# Generated by Django 5.0.7 on 2024-07-13 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="date",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="event",
            name="location",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="event",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name="Ticket",
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
                ("purchaser_name", models.CharField(max_length=100)),
                ("purchase_date", models.DateTimeField(auto_now_add=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="booking.event"
                    ),
                ),
            ],
        ),
    ]
