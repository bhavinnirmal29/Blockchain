# Generated by Django 4.1.1 on 2023-07-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Block",
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
                ("index", models.IntegerField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("data", models.TextField()),
                ("previous_hash", models.CharField(max_length=64)),
                ("hash", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Blockchain",
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
                ("name", models.CharField(max_length=100)),
                ("blocks", models.ManyToManyField(to="Blockchain.block")),
            ],
        ),
    ]
