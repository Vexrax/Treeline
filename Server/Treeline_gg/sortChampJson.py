import json, operator
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



with open(os.path.join(BASE_DIR , '../www/static_data/data_files/champs.json'), 'r') as f:
    data = json.load(f)
    
with open(os.path.join(BASE_DIR , '../www/static_data/data_files/champs.json'), 'w') as out:
    json.dump(data, out, indent=4, sort_keys=True)



