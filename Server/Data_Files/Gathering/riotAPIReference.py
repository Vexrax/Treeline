import requests
import dotenv
import os

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
    res = requests.get(host + "/lol/match/v3/matchlists/by-account/" + str(account_id) + "?queue=470&api_key=" + key)
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
