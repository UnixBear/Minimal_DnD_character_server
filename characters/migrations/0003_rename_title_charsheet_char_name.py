# Generated by Django 4.1.4 on 2023-02-21 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_alter_charsheet_armor_proficiency_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='charsheet',
            old_name='title',
            new_name='char_name',
        ),
    ]
