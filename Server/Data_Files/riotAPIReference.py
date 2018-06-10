import requests
import dotenv
import os
import time

#first load env
env_path = "../../../.env"
dotenv.load_dotenv(dotenv_path=env_path)

#Optional check to ensure it is loaded
#print(os.getenv("TEST_VAR"))

#Assign commonly used vars
host = os.getenv("RIOT_HOST")
key = os.getenv("RIOT_KEY")

######Functions for getting summoner profile##########
#Requires string summoner name and return json
def getSummonerProfileWithName(summoner_name):
    res = requests.get(host + "/lol/summoner/v3/summoners/by-name/" + summoner_name + "?api_key=" + key)
    if not res.ok:
        return Exception(res.status_code)
    return res.json()
#Requires int account ID and returns json
def getSummonerProfileWithAccountID(account_id):
    res = requests.get(host + "/lol/summoner/v3/summoners/by-account/" + str(account_id) + "?api_key=" + key)
    if not res.ok:
        return Exception(res.status_code)
    return res.json()
#requires int summoner ID and returns json
def getSummonerProfileWithSummonerID(summoner_id):
    res = requests.get(host + "/lol/summoner/v3/summoners/" + str(summoner_id) + "?api_key=" + key)
    if not res.ok:
        return Exception(res.status_code)
    return res.json()
###########################################################################

########## Functions for Match Getting ##########
#Requires account ID and return json of match list in ranked twisted treeline queues
def getMatchListForSummonerWithAccountID(account_id):
    res = requests.get(host + "/lol/match/v3/matchlists/by-account/" + str(account_id) + "?beginTime=" + str(os.getenv("PATCH_TIME")) + "&queue=470&api_key=" + key)
    if not res.ok:
        return Exception(res.status_code)
    return res.json()

def getSingleMatchDataWithMatchID(match_id):
    res = requests.get(host + "/lol/match/v3/matches/" + str(match_id) + "?api_key=" + key)
    if not res.ok:
        return Exception(res.status_code)
    return res.json()

def getTimelineWithMatchID(match_id):
    res = requests.get(host + "/lol/match/v3/timelines/by-match/" + str(match_id) + "?api_key=" + key)
    if not res.ok:
        return Exception(res.status_code)
    return res.json()
#################################################################################

######### Functions for getting rank of summoner #########
def getRankOfQueueWithSummonerID(summoner_id, queue):
    res = requests.get(host + "/lol/league/v3/positions/by-summoner/" + str(summoner_id) + "?api_key=" + key)
    if not res.ok:
        return Exception(res.status_code)
    for q in res.json():
        if q["queueType"] == queue:
            return q["tier"]
    return "UNRANKED"

def getRankOfQueueWithAccountID(account_id, queue):
    #Get summoner profile
    temp = getSummonerProfileWithAccountID(account_id)
    if(isinstance(temp, Exception)):
        if(str(temp) == "429"): #Rate limit exceeed
            print("rate limit exceeded. Waiting...")
            time.sleep(20)
            #then try again
            return getRankOfQueueWithAccountID(account_id, queue)
        elif(str(temp) == "401"): #Unauthorized
            #Lol key expired while sleuthing
            print("Key is expired lol")
            quit()
        else:
            #no idea what these would be. Just quit
            quit()
    #Get Summoner Id from profile
    temp = temp["id"]

    #get Rank
    return getRankOfQueueWithSummonerID(temp, queue)

def getChampIDList():
    res = requests.get(host + "/lol/static-data/v3/champions?locale=en_US&champListData=keys&tags=keys&dataById=true&api_key=" + key)
    if not res.ok:
        return Exception(res.status_code)
    return res.json()

def getChampID(champId):
    res = requests.get(host + "/lol/platform/v3/champions/" + champId + "?api_key=" + key)
    if not res.ok:
        return Exception(res.status_code)
    return res.json()

def getChampionData(champId):
    res = requests.get(host + "/lol/static-data/v3/champions/"+ champId + "?locale=en_US&champData=spells&tags=spells&api_key=" + key)
    if not res.ok:
        return Exception(res.status_code)
    return res.json()

