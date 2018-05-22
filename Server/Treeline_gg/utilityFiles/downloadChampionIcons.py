import requests

import json

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#get json of champions
with open('../../../www/static_data/data_files/champs.json') as champFile:
    data = json.load(champFile)
    data = data["data"]

patch = "8.7.1"
#download and write
for key in data:
    print("Downloading image for: " + key)
    img_data = requests.get("http://ddragon.leagueoflegends.com/cdn/" + patch + "/img/champion/" + key + ".png")
    if not (img_data.ok):
        print("Problem downloading image for: " + key)
    else:
        with open('../../../www/static_data/icons/' + key + '.png', 'wb') as img:
            img.write(img_data.content)
            print("Done downloading image for: " + key)
        