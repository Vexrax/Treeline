from os.path import join, dirname
import os
import sys, dotenv
import json
import requests
import riotAPIReference
import time

envpath = join(dirname(__file__), '../../../.env')

dotenv.load_dotenv(dotenv_path=envpath)
#takes up to 2 commandline arguments
#first one should be a summoner name which will act as a seed
#the second one is optional and the database will be filled up until this number
seed_name = ""
max_number = 1000

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

if not(isinstance(max_number, (int))):
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

##Define required functions
def fileGameData(game):
    game_data = riotAPIReference.getSingleMatchDataWithMatchID(game["gameId"])
    #error check to ensure game was gotten correct
    if(isinstance(game_data, Exception)):
        if(str(game_data) == "429"): #Rate limit exceeed
            time.sleep(5)
            #then try again
            fileGameData(game)
        elif(str(game_data) == "401"): #Unauthorized
            #Lol key expired while sleuthing
            print("Key is expired lol")
            quit()
        else:
            #no idea what these would be. Just quit
            quit()
    #do some stuff to actually put the game data into the sqlite table
    #Stuff with matchlists will likely be done it its own file due to the code and work it will require
    #Also don't forget to add summoners to list_of_summoners here

go = True
#This should be checking that the current number of games is less than the desired
while go:
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
        fileGameData(game)
    #get next summoner
    current_summoner_accountID = list_of_summoners.pop()
        
        



