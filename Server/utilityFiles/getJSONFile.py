from os.path import join, dirname
import os
import sys, dotenv
import json
import requests

envpath = join(dirname(__file__), '../../.env')

dotenv.load_dotenv(dotenv_path=envpath)

if (len(sys.argv) != 2):
    print("1 argument required. Options are: champions, items, runes, all")
    quit()

response = []
file_name = []
if(sys.argv[1] == "items"):
    response.append(requests.get(os.getenv("RIOT_HOST") + "/lol/static-data/v3/items?locale=en_US&itemListData=all&tags=all&api_key=" + os.getenv("RIOT_KEY")))
    file_name.append("item_data")
elif sys.argv[1] == 'runes':
    response.append(requests.get(os.getenv("RIOT_HOST") + "/lol/static-data/v3/runes?locale=en_US&runeListData=all&tags=all&api_key=" + os.getenv("RIOT_KEY")))
    file_name.append("rune_data")
elif sys.argv[1] == 'champions':
    response.append(requests.get(os.getenv("RIOT_HOST") + "/lol/static-data/v3/champions?locale=en_US&champListData=all&tags=all&dataById=false&api_key=" + os.getenv("RIOT_KEY")))
    file_name.append("champion_data")
elif sys.argv[1] == 'all':
    #Get items
    response.append(requests.get(os.getenv("RIOT_HOST") + "/lol/static-data/v3/items?locale=en_US&itemListData=all&tags=all&api_key=" + os.getenv("RIOT_KEY")))
    file_name.append("item_data")
    #Get runes
    response.append(requests.get(os.getenv("RIOT_HOST") + "/lol/static-data/v3/runes?locale=en_US&runeListData=all&tags=all&api_key=" + os.getenv("RIOT_KEY")))
    file_name.append("rune_data")
    #Get champions
    response.append(requests.get(os.getenv("RIOT_HOST") + "/lol/static-data/v3/champions?locale=en_US&champListData=all&tags=all&dataById=false&api_key=" + os.getenv("RIOT_KEY")))
    file_name.append("champion_data")
else:
    print('Argument not vaild. Options are: champions, items, runes, all')
    quit()
for r in range(0, len(response)):
    if not response[r].ok:
        print(response)
        quit()

    with open('../../www/static_data/data_files/' + file_name[r] + '.json', 'w') as jFile:
        json.dump(response[r].json(), jFile, indent=4)
   
