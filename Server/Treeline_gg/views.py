import json
from django.shortcuts import HttpResponse, render
from django.http import HttpResponseRedirect
from django.template import loader

import os

from django.template.defaulttags import register


def index(request):
    # get current dir
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # open champion json file
    with open(os.path.join(BASE_DIR, '../www/static_data/data_files/champs.json')) as f:
        data = json.load(f)
        data = data["data"]
    
    # patch = "8.7.1"
    
    # loop through json adding id and url
    for key in data:
        data[key]["boxID"] = "champion_" + key
        data[key]["redirect"] = "/champion/" + key
        # data[key]["url"] = "http://ddragon.leagueoflegends.com/cdn/" + patch + "/img/champion/" + key + ".png"
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
    ptree = 8200 #this will be fed in later
    stree = 8100
    with open('../www/static_data/data_files/rune_data.json') as f:
        rune_page_json = json.load(f)
    #the full runepage json needds to be loaded along with the string name of the primary and secondary rune pages
    #An iteratable list of the active runes also is required to be passed
    #this has no error checking, that should be done before passing the values
    context = {
        'runePageJSON': rune_page_json,
        'primaryTree': ptree,
        'secondaryTree': stree,
        'activeRunes': {8214, 8226, 8234, 8232, 8126, 8120},
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
@register.simple_tag
def is_active_rune(active_runes, current_rune):
    for numb in active_runes:
        if numb == current_rune["id"]:
            return current_rune["id"]
    return str(current_rune["id"]) + "_greyscale"
