# Generated by Django 4.1.4 on 2023-02-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charsheet',
            name='armor_proficiency',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='charsheet',
            name='attack_options',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='charsheet',
            name='feats',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='charsheet',
            name='items',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='charsheet',
            name='misc_features',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='charsheet',
            name='spells_known',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='charsheet',
            name='weapon_proficiency',
            field=models.JSONField(null=True),
        ),
    ]
