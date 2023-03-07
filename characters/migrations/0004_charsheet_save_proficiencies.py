# Generated by Django 4.1.4 on 2023-03-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("characters", "0003_remove_charsheet_saves"),
    ]

    operations = [
        migrations.AddField(
            model_name="charsheet",
            name="save_proficiencies",
            field=models.ManyToManyField(
                blank=True,
                choices=[
                    ("str", "Strength"),
                    ("dex", "Dexterity"),
                    ("con", "Constitution"),
                    ("wis", "Wisdom"),
                    ("int", "Intelligence"),
                    ("cha", "Charisma"),
                ],
                to="characters.charsheet",
            ),
        ),
    ]