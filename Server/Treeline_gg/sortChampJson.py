import json, operator
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


with open(os.path.join(BASE_DIR , '../www/static_data/data_files/champs.json')) as f:
    data = json.load(f.read())
    data = data["data"]
    print(data)
    json.dump(f, data)


