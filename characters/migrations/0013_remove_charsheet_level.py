# Generated by Django 4.1.4 on 2023-04-06 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0012_alter_charsheet_classes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charsheet',
            name='level',
        ),
    ]
