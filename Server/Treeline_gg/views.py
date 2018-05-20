from django.shortcuts import HttpResponse, render
from django.template import loader
import json
import os
import collections



def index(request):
    #return HttpResponse("lol")
    #get current dir
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #open champion json file
    with open(os.path.join(BASE_DIR , '../www/static_data/data_files/champs.json')) as f:
        data = json.load(f)

    patch = "8.7.1"
    #loop through json
    for key in data:
        data[key]["boxID"] = "champion_" + key
        data[key]["url"] = "http://ddragon.leagueoflegends.com/cdn/" + patch + "/img/champion/" + key + ".png"
    #create context var
    context = {
        'champions': data,
    }

    #get template
    template = loader.get_template("champPageBlock.html")
    return HttpResponse(template.render(context, request))