# Generated by Django 2.0.5 on 2018-05-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Treeline_gg', '0003_gamesanalyzed_starting_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamesanalyzed',
            old_name='neutral_minons_killed',
            new_name='neutral_minions_killed',
        ),
        migrations.RenameField(
            model_name='gamesanalyzed',
            old_name='neutral_minons_killed_enemy_jungle',
            new_name='neutral_minions_killed_enemy_jungle',
        ),
        migrations.RenameField(
            model_name='gamesanalyzed',
            old_name='neutral_minons_killed_team_jungle',
            new_name='neutral_minions_killed_team_jungle',
        ),
        migrations.AddField(
            model_name='gamesanalyzed',
            name='role',
            field=models.CharField(default='', max_length=15),
        ),
    ]
