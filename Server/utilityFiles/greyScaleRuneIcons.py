import json
from PIL import Image

with open('../../www/static_data/data_files/rune_data.json') as champFile:
    data = json.load(champFile)
#download and write
for key in data:
    #get path
    #print(key["id"])
    img = Image.open('../../www/static_data/icons/runes/path_icons/' + str(key["id"]) + '.png').convert('L')
    img.save('../../www/static_data/icons/runes/path_icons/' + str(key["id"]) + '_greyscale.png')
    print("Done Convering image for: " + str( key['id']))
    
    #get each rune in path
    for key2 in key["slots"]:
        for key3 in key2["runes"]:
            img = Image.open('../../www/static_data/icons/runes/rune_icons/' + str(key3["id"]) + '.png').convert('LA')
            img.save('../../www/static_data/icons/runes/rune_icons/' + str(key3["id"]) + '_greyscale.png')
            print("Done converting image for: " + str(key3["id"]))