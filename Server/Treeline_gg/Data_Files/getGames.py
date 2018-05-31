from os.path import join, dirname
import os
import sys
import time
import json
import dotenv
import riotAPIReference
import django
import math
import analyzeTimeline

# Redirect system import directory up a fewlevels
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
current_dir = os.path.dirname(current_dir)
parent_dir = current_dir
sys.path.insert(0, parent_dir) 

os.environ["DJANGO_SETTINGS_MODULE"] = 'Treeline.settings'
django.setup()

#This is not an error. File runs with this one
#Also needs to come after the djano setup
from Treeline_gg.models import gamesAnalyzed

def addGameToDatabase(game_data, timeline_data, rank_of_game):
    # this is gonna be cancer
    for participant_id in range(1, 7):
        p_data = game_data["participants"][participant_id - 1]
        p_stats = p_data["stats"]
        victory = True if game_data["teams"][math.floor(participant_id/4)]["win"] == "Win" else False
        try:
            var = gamesAnalyzed(
                entry_id=int(str(game_data["gameId"]) + str(participant_id)),
                game_id = game_data["gameId"],
                participant_id=participant_id,
                champ_id=p_data["championId"],
                role=analyzeTimeline.determineRole(timeline_data, game_data, participant_id),
                win=victory,
                champion_level=p_stats["champLevel"],
                game_length=game_data["gameDuration"],
                game_rank=rank_of_game,
                summoner_spell_1=p_data["spell1Id"],
                summoner_spell_2=p_data["spell2Id"],
                item_1=p_stats["item0"],
                item_2=p_stats["item1"],
                item_3=p_stats["item2"],
                item_4=p_stats["item3"],
                item_5=p_stats["item4"],
                item_6=p_stats["item5"],
                trinket=3348,#lol
                starting_items=analyzeTimeline.getStartingItems(timeline_data, participant_id),
                gold_earned=p_stats["goldEarned"],
                cs=p_stats["totalMinionsKilled"],
                neutral_minions_killed=p_stats["neutralMinionsKilled"],
                neutral_minions_killed_team_jungle=p_stats["neutralMinionsKilledTeamJungle"],
                neutral_minions_killed_enemy_jungle=p_stats["neutralMinionsKilledEnemyJungle"],
                kills=p_stats["kills"],
                deaths=p_stats["deaths"],
                assists=p_stats["assists"],
                total_damage_dealt=p_stats["totalDamageDealt"],
                physical_damage_dealt=p_stats["physicalDamageDealt"],
                magic_damage_dealt=p_stats["magicDamageDealt"],
                true_damage_dealt=p_stats["trueDamageDealt"],
                total_damage_dealt_to_champions=p_stats["totalDamageDealtToChampions"],
                physical_damage_dealt_to_champions=p_stats["physicalDamageDealtToChampions"],
                magic_damage_dealt_to_champions=p_stats["magicDamageDealtToChampions"],
                true_damage_dealt_to_champions=p_stats["trueDamageDealtToChampions"],
                damage_to_objectives=p_stats["damageDealtToObjectives"],
                total_damage_taken=p_stats["totalDamageTaken"],
                physical_damage_taken=p_stats["physicalDamageTaken"],
                magic_damage_taken=p_stats["magicalDamageTaken"],
                true_damage_taken=p_stats["trueDamageTaken"],
                cc_duration=p_stats["timeCCingOthers"],
                total_healing=p_stats["totalHeal"],
                primary_tree=1000,
                secondary_tree=2000,
                rune_1=p_stats["perk0"],
                rune_2=p_stats["perk1"],
                rune_3=p_stats["perk2"],
                rune_4=p_stats["perk3"],
                rune_5=p_stats["perk4"],
                rune_6=p_stats["perk5"] 
            )
        except KeyError:
            return
        var.save()

# Testing
# game = ""
# timeline = ""
# with open("../../../www/static_data/data_files/example_game_json.json") as gameJson:
#     game = json.load(gameJson)

# with open("../../../www/static_data/data_files/example_timeline.json") as timelineJson:
#     timeline = json.load(timelineJson)

# addGameToDatabase(game, timeline, 2)
#quit()
envpath = join(dirname(__file__), '../../../.env')
dotenv.load_dotenv(dotenv_path=envpath)
#takes up to 2 commandline arguments
#first one should be a summoner name which will act as a seed
#the second one is optional and the database will be filled up until this number
seed_name = ""
max_number = 1000000

if(len(sys.argv) > 3):
    print("Too many arguments. Requires (summoner_name, [max_entries])")
    exit()
elif(len(sys.argv) <= 1):
    print("Too few arguments. Requires (summoner_name, [max_entries])")
    quit()
elif(len(sys.argv) == 3):
    seed_name = sys.argv[1]
    max_number = sys.argv[2]
else: # 1 extra arg
    seed_name = sys.argv[1]

if not(isinstance(max_number, int)):
    print("Second argument must be a whole number")
    exit()

##done input parsing
##first get summoner data
summonerData = riotAPIReference.getSummonerProfileWithName(seed_name)
#Ensure data is valid
if(isinstance(summonerData, Exception)):
    print("Summoner inputted was not a valid seed. Summoner doesn't exisit")
    quit()
#At this point we should have a confimred summoner seed and data sleuthing can begin

#Set up some variables
current_summoner_accountID = summonerData["accountId"]
current_summoner_matchlist = ""
list_of_summoners = [] #This is a list of summoners found who will be explored after exausting current summmoner's games
list_of_visited_summoners = [] # Just so we don't recheck old ones

##Define required functions
def fileGameData(game, current_account_id, current_rank):
    game_data = riotAPIReference.getSingleMatchDataWithMatchID(game["gameId"])
    game_timeline = riotAPIReference.getTimelineWithMatchID(game["gameId"])
    #error check to ensure game was gotten correct
    if(isinstance(game_data, Exception)):
        if(str(game_data) == "429"): #Rate limit exceeed
            print("rate limit exceeded. Waiting...")
            time.sleep(20)
            #then try again
            fileGameData(game, current_account_id, current_account_id)
            return
        elif(str(game_data) == "401"): #Unauthorized
            #Lol key expired while sleuthing
            print("Key is expired lol")
            quit()
        else:
            #no idea what these would be. Just quit
            quit()
    if(isinstance(game_timeline, Exception)):
        if(str(game_timeline) == "429"): #Rate limit exceeed
            time.sleep(10)
            #then try again
            fileGameData(game, current_account_id, current_rank)
            return
        elif(str(game_timeline) == "401"): #Unauthorized
            #Lol key expired while sleuthing
            print("Key is expired lol")
            quit()
        else:
            #no idea what these would be. Just quit
            quit()
    
    #do some stuff to actually put the game data into the sqlite table
    #Stuff with matchlists will likely be done it its own file due to the code and work it will require
    #Also don't forget to add summoners to list_of_summoners here

    for participant in game_data["participantIdentities"]:
        if(participant["player"]["accountId"] != current_account_id):
            #If the player we are looking at isn't the player whose matchlist we are going through add em to list to check
            if(len(list_of_summoners) < 100) and participant["player"]["accountId"] not in list_of_summoners and participant["player"]["accountId"] not in list_of_visited_summoners:
                list_of_summoners.append(participant["player"]["accountId"])
        addGameToDatabase(game_data, game_timeline, current_rank)

go = True
#This should be checking that the current number of games is less than the desired
while len(gamesAnalyzed.objects.filter()) <= max_number:
    go = False#For testing just loop through once
    #Get current summoner matchlist
    current_summoner_matchlist = riotAPIReference.getMatchListForSummonerWithAccountID(current_summoner_accountID)
    #if there is no data or some other error
    if(isinstance(current_summoner_matchlist, Exception)):
        if(str(current_summoner_matchlist) == "429"): #Rate limit exceeded
            time.sleep(5) #sleep for 5 seconds then try again
            continue
        elif(str(current_summoner_matchlist) == "401"): #Unauthorized
            print("The key is invalid")
            quit()
        elif(str(current_summoner_matchlist) == "404" or str(current_summoner_matchlist) == "422"):
            print("No data for current summoner")
            if(len(list_of_summoners) == 0):
                quit()
            current_summoner_accountID = list_of_summoners.pop()
            continue
    #If there is no error
    #go over each game in the matchList
    for game in current_summoner_matchlist["matches"]:
        list_of_visited_summoners.append(current_summoner_accountID)
        rank = riotAPIReference.getRankOfQueueWithAccountID(current_summoner_accountID, "RANKED_FLEX_TT")
        fileGameData(game, current_summoner_accountID, rank)
    #get next summoner
    current_summoner_accountID = list_of_summoners.pop()
    
    time.sleep(3) #sleep to try and prevent going over rate limit        



