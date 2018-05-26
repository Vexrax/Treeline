from os.path import join, dirname
import os
import sys, dotenv
import json
import requests

envpath = join(dirname(__file__), '../../../.env')

dotenv.load_dotenv(dotenv_path=envpath)
#takes up to 2 commandline arguments
#first one should be a summoner name which will act as a seed
#the second one is optional and the database will be filled up until this number
seed_name = ""
max_number = 0

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
riot_key = os.getenv("RIOT_KEY")
summoner_data_url = os.getenv("RIOT_HOST") + "/something" + seed_name + "something" + riot_key

response = requests.get(summoner_data_url)
if not(response.ok):
    print("Something happened")
    exit()

#verify that the summoner was found

summoner = response.json()
if not(type(summoner) == dict):
    print("Response was not what was expected. Url accessed was " + summoner_data_url)

#At this point we should have a confimred summoner seed and data sleuthing can begin