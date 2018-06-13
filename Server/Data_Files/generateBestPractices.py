from enum import Enum
from collections import Counter
import os
import sys
import json
import django
import itertools
# Redirect system import directory up a fewlevels
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# current_dir = os.path.dirname(current_dir)
parent_dir = current_dir
sys.path.insert(0, parent_dir) 
print(parent_dir)

os.environ["DJANGO_SETTINGS_MODULE"] = 'Treeline.settings'
django.setup()

#This is not an error. File runs with this one
#Also needs to come after the djano setup
from Treeline_gg.models import gamesAnalyzed, bestPractices

#these will be globals so they can be carried over
timeline = ""
timeline_game_id = 0
item_data = ""
# Load item data. Will be used for costing
with open("../../www/static_data/data_files/item_data.json") as item_file:
    item_data = json.load(item_file)["data"]
class roles(Enum):
    Top = 0
    Jungle = 1
    Bottom = 2
    Hyper = 3
    Support = 4

def run(champion_id):
    res = gamesAnalyzed.objects.filter(champ_id=champion_id)
    
    if(len(res) < 30):
        # if there are less than x datapoints there is not enough data
        return -1
    # just get playrate now. Times 6 cuz 6 players in a game so about 6 datapoints per game
    # Not perfect because some datapoints had issues so a bit less than 6 per game. But rounding lol


    role_counts = [0, 0, 0, 0, 0] # a count of role positions: top, jungle, bottom, carry, support
    curRoles = [0, 0]

    # Get primary and secondary roles
    for game in res:
        if(game.role == "Undetermined"): 
            continue
        role_counts[roles[game.role].value] += 1
    
    for i in range(len(role_counts)):
        if(role_counts[i] > role_counts[curRoles[0]]):
            curRoles[1] = curRoles[0]
            curRoles[0] = i
    if(role_counts[curRoles[0]] < 30):
        return -1
    if(role_counts[curRoles[1]] < 30):
        curRoles[1] = -1


    # get games for primary role
    res = gamesAnalyzed.objects.filter(champ_id=champion_id, role=roles(curRoles[0]).name)
    do_games_with_list(res, curRoles[0], "Primary")
    if(curRoles[1] == -1): return
    res = gamesAnalyzed.objects.filter(champ_id=champion_id, role=roles(curRoles[1]).name)
    do_games_with_list(res, curRoles[1], "Secondary")

def do_games_with_list(res, role, r_type):
    playrate = (len(res) * 6) / gamesAnalyzed.objects.count()
    summoner_spells = [] # a list of spells. a tally will be done at the end
    starting_items = [] # same deal
    ending_items = []
    skill_order = []
    rune_trees = []
    primary_tree = []
    secondary_tree = []
    wins = 0

    # gather data from database
    for game in res:
        summoner_spells.append(game.summoner_spell_1)
        summoner_spells.append(game.summoner_spell_2)
        if(game.win): wins += 1
        
        starting_items.append(game.starting_items)

        ending_items.append(game.item_1)
        ending_items.append(game.item_2)
        ending_items.append(game.item_3)
        ending_items.append(game.item_4)
        ending_items.append(game.item_5)
        ending_items.append(game.item_6)

        skill_order.append(game.skilling_order[0:25])
        rune_trees.append({"primaryTree": game.primary_tree, 
                        "secondaryTree": game.secondary_tree,
                        "primaryRunes": [game.rune_1, game.rune_2, game.rune_3, game.rune_4],
                        "secondaryRunes": [game.rune_5, game.rune_6]})
    win_rate = wins / len(res)
    # ITEMS
    # Starting items
    most_common_starting_items = Counter(starting_items).most_common()[0][0]
    #Ending items
    while(0 in ending_items):
        ending_items.remove(0)
    common_end_items = Counter(ending_items).most_common()
    most_common_ending_items = []
    for i in range(len(common_end_items)):
        if(item_data[str(common_end_items[i][0])]["gold"]["total"] > 2000):
            most_common_ending_items.append(common_end_items[i][0])
        if(len(most_common_ending_items) >= 3):
            break
    # RUNE TREES
    # determine most common rune tree
    commonRunes = {}
    for entry in rune_trees:
        string_eq = str(entry["primaryTree"]) + "," + str(entry["secondaryTree"])
        if(commonRunes.get(string_eq) is None):
            commonRunes[string_eq] = 1
        else:
            commonRunes[string_eq] += 1

    most_common_trees = max(commonRunes, key=commonRunes.get)
    string_eq = str(most_common_trees)
    # determine most common runes in said tree
    # Lets take most common rune in each tier
    most_common_runes = [[], [], [], [], [], []]
    for entry in rune_trees:
        if(int(string_eq.split(',')[0]) == int(entry["primaryTree"])):
            most_common_runes[0].append(entry["primaryRunes"][0])
            most_common_runes[1].append(entry["primaryRunes"][1])
            most_common_runes[2].append(entry["primaryRunes"][2])
            most_common_runes[3].append(entry["primaryRunes"][3])
        if(int(string_eq.split(',')[1]) == int(entry["secondaryTree"])):
            most_common_runes[4].append(entry["secondaryRunes"][0])
            most_common_runes[5].append(entry["secondaryRunes"][1])
    # get most common runes
    for i in range(len(most_common_runes)):
        most_common_runes[i] = Counter(most_common_runes[i]).most_common(1)[0][0]
    # print(most_common_runes)
    var = bestPractices(
        event_id = int(str(res[0].champ_id) + str(role)),
        champ_id = res[0].champ_id,
        winrate = win_rate,
        playrate = playrate,
        games_played = len(res),
        role_type = r_type,
        role = roles(role).name,
        starting_items = most_common_starting_items,
        final_items = most_common_ending_items,
        skilling_order = Counter(skill_order).most_common(1)[0][0],
        rune_trees = string_eq,
        tree_1 = ','.join(map(str, most_common_runes[0:4])),
        tree_2 = ','.join(map(str, most_common_runes[4:6]))
    )
    var.save()


champs = ""
with open("../../www/static_data/data_files/champion_data.json") as champData:
    champs = json.load(champData)["data"]

for champ in champs:
    run(champs[champ]["id"])
    print("Finished " + champ)

