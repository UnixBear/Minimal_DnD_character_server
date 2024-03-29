# Generated by Django 4.1.4 on 2023-03-28 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0007_charsheet_speed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charsheet',
            name='character_class',
            field=models.CharField(choices=[('Barbarian', 'Barbarian'), ('Bard', 'Bard'), ('Cleric', 'Cleric'), ('Druid', 'Druid'), ('Fighter', 'Fighter'), ('Monk', 'Monk'), ('Paladin', 'Paladin'), ('Ranger', 'Ranger'), ('Rogue', 'Rogue'), ('Sorcerer', 'Sorcerer'), ('Warlock', 'Warlock'), ('Wizard', 'Wizard')], default='Barbarian', max_length=45),
        ),
    ]
