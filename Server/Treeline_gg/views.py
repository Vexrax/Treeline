import json, operator
from django.shortcuts import HttpResponse, render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

import os
import collections

from django.shortcuts import HttpResponse, render
from django.template import loader
from django.template.defaulttags import register



def index(request):
    #get current dir
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #open champion json file
    with open(os.path.join(BASE_DIR , '../www/static_data/data_files/champs.json')) as f:
        data = json.load(f)
        data = data["data"]
    
    #patch = "8.7.1"
    
    #loop through json adding id and url
    for key in data:
        data[key]["boxID"] = "champion_" + key
        data[key]["redirect"] = "/champion/" + key
        #data[key]["url"] = "http://ddragon.leagueoflegends.com/cdn/" + patch + "/img/champion/" + key + ".png"
        data[key]["url"] = "/static/icons/champions/" + key + ".png"

    #print(data)
    #create context var
    context = {
        'champions': data,
    }
    
    #get template
    template = loader.get_template("homePage.html")
    return HttpResponse(template.render(context, request))

#redirect searches
def handle_search(request):
    if request.method == "POST":
        return HttpResponseRedirect('/champion/' + request.POST.get("title", ""))
    else:
        renderchamp(request)
        return render(request, 'championpage.html')

def renderchamp(request):
    print("rendering champ data")

def test_page(request):
    ttree = "Domination" #this will be fed in later

    ##this section needs to be loaded for every runepage
    with open('../www/static_data/data_files/rune_data.json') as f:
        rune_page_json = json.load(f)
    for tree in rune_page_json:
        if(tree["key"] == ttree):
            rune_page_json = tree
    context = {
        'runePageJSON': rune_page_json,
    }
    ##end sections

    template = loader.get_template("testpage.html")
    return HttpResponse(template.render(context, request))

#create custom tags for later use
#these are just to get data from the dict created above
@register.simple_tag
def get_item(myDict, key):
    return myDict.get(key)
@register.simple_tag
def get_boxID(myDict, key):
    return myDict.get(key).get("boxID")
@register.simple_tag
def get_url(myDict, key):
    return myDict.get(key)["url"]
@register.simple_tag
def get_redirect(myDict, key):
    return myDict.get(key).get("redirect")
@register.simple_tag
def get_name(myDict, key):
    return myDict.get(key).get("name")
