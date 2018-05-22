import json
from PIL import Image

#get json of champions
with open('../../../www/static_data/data_files/champs.json') as champFile:
    data = json.load(champFile)
    data = data["data"]

for key in data:
    print('Converting image for ' + key)
    img = Image.open('../../../www/static_data/data_files/icons/' + key + '.png').convert('LA')
    img.save('../../../www/static_data/data_files/icons/' + key + '_greyscale.png')
    print('... done')
