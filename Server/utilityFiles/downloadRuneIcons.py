import requests

import json

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#get json of champions
with open('../../www/static_data/data_files/rune_data.json') as champFile:
    data = json.load(champFile)

#download and write
for key in data:
    #get path
    #print(key["id"])
    img_data = requests.get("https://ddragon.leagueoflegends.com/cdn/img/" + key["icon"])

    if not (img_data.ok):
        print("Problem downloading image for: " + str(key["id"]))
    else:
        with open('../../www/static_data/icons/runes/path_icons/' + str(key["id"]) + '.png', 'wb') as img:
            img.write(img_data.content)
            print("Done downloading image for: " +str( key['id']))
    
    #get each rune in path
    for key2 in key["slots"]:
        for key3 in key2["runes"]:
            img_data = requests.get("https://ddragon.leagueoflegends.com/cdn/img/" + key3["icon"])

            if not (img_data.ok):
                print("Problem downloading image for: " + str(key3["id"]))
            else:
                with open('../../www/static_data/icons/runes/rune_icons/' + str(key3["id"]) + '.png', 'wb') as img:
                    img.write(img_data.content)
                    print("Done downloading image for: " + str(key3["id"]))