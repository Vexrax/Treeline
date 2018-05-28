# Generated by Django 2.0.5 on 2018-05-28 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bestPractices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champ_id', models.SmallIntegerField()),
                ('role_1', models.CharField(max_length=10)),
                ('role_2', models.CharField(max_length=10)),
                ('startingItems', models.CharField(max_length=30)),
                ('finalItems', models.CharField(max_length=30)),
                ('skillingOrder', models.CharField(max_length=30)),
                ('rune_trees', models.CharField(max_length=30)),
                ('tree_1', models.CharField(max_length=30)),
                ('tree_2', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='champions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champ_name', models.CharField(max_length=25)),
                ('champ_id', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='gamesAnalyzed',
            fields=[
                ('entry_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('game_id', models.IntegerField()),
                ('participant_id', models.SmallIntegerField()),
                ('champ_id', models.SmallIntegerField()),
                ('game_length', models.BigIntegerField()),
                ('win', models.BooleanField()),
                ('champion_level', models.SmallIntegerField()),
                ('summoner_spell_1', models.SmallIntegerField()),
                ('summoner_spell_2', models.SmallIntegerField()),
                ('item_1', models.SmallIntegerField()),
                ('item_2', models.SmallIntegerField()),
                ('item_3', models.SmallIntegerField()),
                ('item_4', models.SmallIntegerField()),
                ('item_5', models.SmallIntegerField()),
                ('item_6', models.SmallIntegerField()),
                ('trinket', models.SmallIntegerField()),
                ('gold_earned', models.SmallIntegerField()),
                ('cs', models.SmallIntegerField()),
                ('neutral_minons_killed', models.SmallIntegerField()),
                ('neutral_minons_killed_team_jungle', models.SmallIntegerField()),
                ('neutral_minons_killed_enemy_jungle', models.SmallIntegerField()),
                ('kills', models.SmallIntegerField()),
                ('deaths', models.SmallIntegerField()),
                ('assists', models.SmallIntegerField()),
                ('total_damage_dealt', models.IntegerField()),
                ('physical_damage_dealt', models.IntegerField()),
                ('magic_damage_dealt', models.IntegerField()),
                ('true_damage_dealt', models.IntegerField()),
                ('total_damage_dealt_to_champions', models.IntegerField()),
                ('physical_damage_dealt_to_champions', models.IntegerField()),
                ('magic_damage_dealt_to_champions', models.IntegerField()),
                ('true_damage_dealt_to_champions', models.IntegerField()),
                ('damage_to_objectives', models.IntegerField()),
                ('total_damage_taken', models.IntegerField()),
                ('physical_damage_taken', models.IntegerField()),
                ('magic_damage_taken', models.IntegerField()),
                ('true_damage_taken', models.IntegerField()),
                ('cc_duration', models.SmallIntegerField()),
                ('total_healing', models.SmallIntegerField()),
                ('primary_tree', models.SmallIntegerField()),
                ('secondary_tree', models.SmallIntegerField()),
                ('rune_1', models.SmallIntegerField()),
                ('rune_2', models.SmallIntegerField()),
                ('rune_3', models.SmallIntegerField()),
                ('rune_4', models.SmallIntegerField()),
                ('rune_5', models.SmallIntegerField()),
                ('rune_6', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='bestpractices',
            name='champ_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Treeline_gg.champions'),
        ),
    ]
